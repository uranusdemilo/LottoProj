import operator
import statistics

class matrix:
    def __init__(self):
        self.col=[0]
        self.ball=[0]
        self.numBalls=47
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(27))
        self.leastCommonBall=0
        self.leastCommonHits=0
        self.mostCommonBall=0
        self.mostCommonHits=0
        self.unsortedHits={}
        self.sortedHits={}
        self.firstDraw=1375
        self.lastDraw=0
        self.numDraws=0
        self.meanDist=0
        for b in range(1,48):
            self.ball.append(lottoBall(b)) #instantiate ball b
        for b in range(1,48):
            self.unsortedHits[b]=0  #create unsortedHits dictionary

    def sorthits(self):
            self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))

class col:
    def __init__(self,numBalls):
        self.numBalls=numBalls
        self.ball=[0]
        self.leastHits=1000
        self.mostHits=0
        self.leastCommonBall=0
        self.leastCommonHits=0
        self.mostCommonBall=0
        self.mostCommonHits=0
        self.unsortedHits={}
        self.sortedHits={}
        ###Instantiate Balls in Row
        for b in range(1,numBalls + 1):
            self.ball.append(lottoBall(b)) #instantiate ball b
        for b in range(1,self.numBalls+1):
            self.unsortedHits[b]=0  #create unsortedHits dictionary
    def sorthits(self):
        self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))
        
class lottoBall:
    def __init__(self, number):
        self.number=number
        self.hits=0
        #self.score=0 commented 2/13 - not used
        self.hitMatrix=[]
        self.diffMatrix=[]
        self.meanDist=0
        self.sdevDist=0 #Standard Deviation for Distance Vector
        self.diffPull=0
        self.lastHit=0
        self.lastDiffs=[]
        self.probScore=0

    def appendHitMatrix(self,draw):
        self.hitMatrix.append(draw)

    def getMeanDist(self):
        self.meanDist=statistics.mean(self.diffMatrix)

def file_len(fname): #Get Nuber of Draws in File
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def showprob(col):
    for x in range(1,47):
        print(str(x) + " " + str(slp.col[col].ball[x].probScore))

slp=matrix()
drawAndDate=[]
charLineData=[]
testLen=100
slp.numDraws=file_len("allnumbers.txt")
slp.lastDraw=slp.firstDraw + slp.numDraws - 1
inFile=open("allnumbers.txt")
for drawNum in range(slp.firstDraw,slp.lastDraw - testLen + 1): #loop through draws
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    currentBallIndex=0
    for x in range(1,7):
        currentBallIndex=int(charLineData[x])
        slp.col[x].ball[currentBallIndex].appendHitMatrix(drawNumber) #append number to balls HitMatrix
        slp.col[x].ball[currentBallIndex].hits += 1 #add 1 to ball-column hitlist
        slp.ball[currentBallIndex].hits += 1        #add 1 to ball-matrix hitlist
        if slp.col[x].ball[currentBallIndex].lastHit != 0:
            currentDiffCol=drawNumber -(slp.col[x].ball[currentBallIndex].lastHit)
        else:
            currentDiffCol=drawNumber-(slp.firstDraw)
        if(x != 6):                                 # col 6 is Mega....don't include in matrix
            if slp.ball[currentBallIndex].lastHit !=0:
                currentDiffMat=drawNumber -(slp.ball[currentBallIndex].lastHit)
            else:
                currentDiffMat=drawNumber-slp.firstDraw
            slp.ball[currentBallIndex].diffMatrix.append(currentDiffMat)
            slp.ball[currentBallIndex].diffMatrix.append(currentDiffMat)
            slp.ball[currentBallIndex].lastHit=drawNumber
        slp.col[x].ball[currentBallIndex].diffMatrix.append(currentDiffCol)
        slp.col[x].ball[currentBallIndex].lastHit=drawNumber
        slp.col[x].unsortedHits[currentBallIndex] += 1
        slp.unsortedHits[currentBallIndex] += 1
slp.lastDraw=drawNumber
for c in range(1,7):   #sortingHitsColumn, sort all sortedHits lists in Col objects
    slp.col[c].sorthits()
    slp.sorthits()
for c in range(1,7):
    slp.col[c].mostCommonBall=slp.col[c].sortedHits[slp.col[c].numBalls - 1][0]
    slp.col[c].mostCommonHits=slp.col[c].sortedHits[slp.col[c].numBalls - 1][1]
    slp.col[c].leastCommonBall=slp.col[c].sortedHits[0][0]
    slp.col[c].leastCommonHits=slp.col[c].sortedHits[0][1]
slp.mostCommonBall=slp.sortedHits[slp.numBalls - 1][0]
slp.mostCommonHits=slp.sortedHits[slp.numBalls - 1][1]
slp.leastCommonBall=slp.sortedHits[0][0]
slp.leastCommonHits=slp.sortedHits[0][1]
    
for c in range(1,7):
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].getMeanDist()
        if(b == 1):
           slp.ball[b].getMeanDist()
for testNum in range(0,testLen):
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
for c in range(1,7):                            #Calculate Mean Difference of all balls.
    for b in range(1,slp.col[c].numBalls + 1):
       freqScore=(slp.col[c].ball[b].hits - slp.col[c].leastCommonHits)/(slp.col[c].mostCommonHits - slp.col[c].leastCommonHits)
       slp.col[c].ball[b].probScore += freqScore
