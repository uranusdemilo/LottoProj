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

fileData=[]
lineData=[]
drawAndDate=[]
charLineData=[]
#intLineData=[] Commented out 12/4
unSortedHits={}
slp=matrix()
matrixLength=0
inFile=open("allnumbers.txt")
rawFileData=reversed(inFile.readlines())
for rawLineData in rawFileData:
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    matrixLength+=1
    for x in range(1,7):
        slp.col[x].ball[int(charLineData[x])].hitMatrix.append(drawNumber) #append number to balls hitMatrix
        slp.col[x].ball[int(charLineData[x])].hits += 1 #add 1 to balls hitlist
        slp.col[x].ball[int(charLineData[x])].lastHit=drawNumber
slp.lastDraw=drawNumber

        
