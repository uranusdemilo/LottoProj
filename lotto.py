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
        self.leastCommon=0
        self.mostCommon=0
        self.sortedHits=[]
        ###Instantiate Balls in Row
        for x in range(1,numBalls + 1):
            self.ball.append(lottoBall(x))
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

drawAndDate=[]
charLineData=[]
testLen=100
slp=matrix()
slp.numDraws=file_len("allnumbers.txt")
slp.lastDraw=slp.firstDraw + slp.numDraws - 1
inFile=open("allnumbers.txt")
for drawNum in range(slp.firstDraw,slp.lastDraw - testLen):
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
slp.lastDraw=drawNumber
#for testNum in range(1,testLen):
#   rawLineData=infFile.readline()
#    charLineData=rawLineData.split('          ') #split number fields
#    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
#    drawNumber=int(drawAndDate[0])

        
