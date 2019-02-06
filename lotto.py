import operator

class matrix:
    def __init__(self):
        self.col=[0]
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(27))
        self.firstDraw=1375
        self.lastDraw=0
        self.numDraws=0
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
        for bn in range(1,numBalls + 1):
            self.ball.append(lottoBall(bn))
        for bu in range(1,self.numBalls+1):
            self.unsortedHits[bu]=0
    def sorthits(self):
        self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))
        
class lottoBall:
    def __init__(self, number):
        self.number=number
        self.hits=0
        self.score=0
        self.hitMatrix=[]
        self.diffMatrix=[]
        self.meanDist=0
        self.sdevDist=0 #Standard Deviation for Distance Vector
        self.diffPull=0
        self.lastHit=0
        self.lastDiffs=[]
        self.probScore=0

def file_len(fname): #Get Nuber of Draws in File
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

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
        slp.col[x].ball[currentBallIndex].hitMatrix.append(drawNumber) #append number to balls hitMatrix
        slp.col[x].ball[currentBallIndex].hits += 1 #add 1 to balls hitlist
        if slp.col[x].ball[currentBallIndex].lastHit != 0:
            currentDiff=drawNumber -(slp.col[x].ball[currentBallIndex].lastHit)
        else:
            currentDiff=drawNumber-(slp.firstDraw)
        slp.col[x].ball[currentBallIndex].diffMatrix.append(currentDiff)
        slp.col[x].ball[currentBallIndex].lastHit=drawNumber
        slp.col[x].unsortedHits[currentBallIndex]+=1
slp.lastDraw=drawNumber
for shc in range(1,7):   #sortingHitsColumn, sort all sortedHits lists in Col objects
    slp.col[shc].sorthits()
for lmc in range(1,7):
    slp.col[lmc].mostCommonBall=slp.col[lmc].sortedHits[slp.col[lmc].numBalls - 1][0]
    slp.col[lmc].mostCommonHits=slp.col[lmc].sortedHits[slp.col[lmc].numBalls - 1][1]
    slp.col[lmc].leastCommonBall=slp.col[lmc].sortedHits[0][0]
    slp.col[lmc].leastCommonHits=slp.col[lmc].sortedHits[0][1]
for testNum in range(0,testLen):
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
for c in range(1,7):
    for b in range(1,slp.col[c].numBalls + 1):
       freqScore=(slp.col[c].ball[b].hits - slp.col[c].leastCommonHits)/slp.col[c].mostCommonHits
       slp.col[c].ball[b].probScore += freqScore
