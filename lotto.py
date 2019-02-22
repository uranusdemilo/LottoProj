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
        
    def appendHitMatrix(self,draw):
        self.hitMatrix.append(draw)

    def getLeastAndMostCommon(self):
        self.mostCommonBall=self.sortedHits[slp.numBalls - 1][0]
        self.mostCommonHits=self.sortedHits[slp.numBalls - 1][1]
        self.leastCommonBall=self.sortedHits[0][0]
        self.leastCommonHits=self.sortedHits[0][1]
                
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
        self.total=0
        ###Instantiate Balls in Row
        for b in range(1,self.numBalls + 1):
            self.ball.append(lottoBall(b)) #instantiate ball b
        for b in range(1,self.numBalls+1):
            self.unsortedHits[b]=0  #create unsortedHits dictionary
         
    def sorthits(self):
        self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))

    def getLeastAndMostCommon(self):
        self.mostCommonBall=self.sortedHits[self.numBalls - 1][0]
        self.mostCommonHits=self.sortedHits[self.numBalls - 1][1]
        self.leastCommonBall=self.sortedHits[0][0]
        self.leastCommonHits=self.sortedHits[0][1]

    def seeColDiffs(self):
        for b in range(1,self.numBalls + 1):
            print(str(b) + "   "  + str(self.ball[b].diffScore))

    def aveColDiff(self):
        for b in range(1,self.numBalls + 1):
            self.total += self.ball[b].diffScore
            
class lottoBall:
    def __init__(self, number):
        self.number=number
        self.hits=0
        self.hitMatrix=[]
        self.diffMatrix=[]
        self.meanDiv=0
        self.sdevDiv=0 #Standard Deviation for Distance Vector
        self.diffPull=0
        self.lastHit=0
        self.numDiffs=0
        self.lastThreeDiffs=[]
        self.probScore=0
        self.diffScore=0

    def appendHitMatrix(self,draw):
        self.hitMatrix.append(draw)

    def getMeanDist(self):
        self.meanDiv=statistics.mean(self.diffMatrix) - 15

    def getLastThreeDiffs(self):
        self.numDiffs=len(self.diffMatrix)
        for x in range(self.numDiffs - 3,self.numDiffs):
            self.lastThreeDiffs.append(self.diffMatrix[x])
    def getDiffScore(self):
        if self.lastThreeDiffs[1] < self.meanDiv:
            self.diffScore -= .1
        if self.lastThreeDiffs[2] < self.meanDiv:
            self.diffScore -= .1
        if self.lastThreeDiffs[1] < self.meanDiv and self.lastThreeDiffs[2] < self.meanDiv:
            self.diffScore -= .1
        if self.lastThreeDiffs[1] > self.meanDiv:
            self.diffScore += .1
        if self.lastThreeDiffs[2] > self.meanDiv:
            self.diffScore += .1
        if self.lastThreeDiffs[1] > self.meanDiv and self.lastThreeDiffs[2] < self.meanDiv:
            self.diffScore += .1
        
def file_len(fname): #Get Number of Draws in File
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def showprob(col):
    for x in range(1,47):
        print(str(x) + " " + str(slp.col[col].ball[x].probScore))
def showdiffs(c):
    for c in range(1,7):
        slp.col[c].seeDiffScores()
def showDiffAves():
    for c in range(1,7):
        sumDiffs = 0
        for b in range(1,slp.col[c].numBalls + 1):
           sumDiffs += slp.col[c].ball[b].diffScore
        print("col " + str(c) + " = " + str(sumDiffs))

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
    for x in range(1,7):  # read one line at time, feed each number into balls
        currentBallIndex=int(charLineData[x])
        slp.col[x].ball[currentBallIndex].appendHitMatrix(drawNumber) #append number to balls HitMatrix
        slp.ball[currentBallIndex].appendHitMatrix(drawNumber)
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
    slp.col[c].getLeastAndMostCommon()
    slp.getLeastAndMostCommon()
    
for c in range(1,7): #Get Last Three Diff Entries
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].getMeanDist()
        slp.col[c].ball[b].getLastThreeDiffs()
        if(c == 1):   # do matrix balls only once, no cols
           slp.ball[b].getMeanDist()
           slp.ball[b].getLastThreeDiffs()
####Start Scoring Columns and Matrix#####
for c in range(1,7):  #Frequency Scoring
    for b in range(1,slp.col[c].numBalls + 1):
        freqScore=(slp.col[c].ball[b].hits - slp.col[c].leastCommonHits)/(slp.col[c].mostCommonHits - slp.col[c].leastCommonHits)  #i
        slp.col[c].ball[b].probScore += freqScore
        if c == 1:
            freqScore=(slp.ball[b].hits - slp.leastCommonHits)/(slp.mostCommonHits - slp.leastCommonHits)  #i
            slp.ball[b].probScore += freqScore

for c in range(1,7):
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].getDiffScore()

for testNum in range(0,testLen):
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
