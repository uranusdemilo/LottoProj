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
        self.mostRecentDraw=1375
        self.unsortedHits={}
        self.unsortedScores={}
        self.sortedHits={}
        self.firstDraw=1375
        self.lastDraw=0
        self.numDraws=0
        self.meanDist=0
        self.mostProbable=[]
        for b in range(1,48):
            self.ball.append(lottoBall(b)) #instantiate ball b
        for b in range(1,48):
            self.unsortedHits[b]=0  #create unsortedHits dictionary

    def sortHits(self):
        self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))

    def sortScores(self):
        self.sortedScores=sorted(self.unsortedScores.items(), key=operator.itemgetter(1))
        
    def appendHitMatrix(self,drawn):
        self.hitMatrix.append(drawn)

    def getLeastAndMostCommon(self):
        self.mostCommonBall=self.sortedHits[slp.numBalls - 1][0]
        self.mostCommonHits=self.sortedHits[slp.numBalls - 1][1]
        self.leastCommonBall=self.sortedHits[0][0]
        self.leastCommonHits=self.sortedHits[0][1]

    def getUnsortedScores(self):
        for b in range(1,47):
            self.unsortedScores[b]=self.ball[b].probScore

    def totalUpScore(self):
        self.probScore=self.freqScore + self.diffScore

    def getMostProbable(self):
        for c in range(1,7):
            if c < 6:
                self.mostProbable.append(slp.col[c].sortedScores[46][0])
            else:
                self.mostProbable.append(slp.col[c].sortedScores[26][0])

        
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
        self.unsortedScores={}
        self.sortedScores={}
        self.sortedHits={}
        self.total=0
        ###Instantiate Balls in Row
        for b in range(1,self.numBalls + 1):
            self.ball.append(lottoBall(b)) #instantiate ball b
        for b in range(1,self.numBalls+1):
            self.unsortedHits[b]=0  #create unsortedHits dictionary
         
    def sortHits(self):
        self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))

    def sortScores(self):
        self.sortedScores=sorted(self.unsortedScores.items(), key=operator.itemgetter(1))
    
    def getLeastAndMostCommon(self):
        self.mostCommonBall=self.sortedHits[self.numBalls - 1][0]
        self.mostCommonHits=self.sortedHits[self.numBalls - 1][1]
        self.leastCommonBall=self.sortedHits[0][0]
        self.leastCommonHits=self.sortedHits[0][1]

    def getUnsortedScores(self):
        for b in range(1,self.numBalls + 1):
            self.unsortedScores[b]=self.ball[b].probScore

    def seeColDiffs(self):
        for b in range(1,self.numBalls + 1):
            print(str(b) + "   "  + str(round(self.ball[b].diffScore,3)))

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
        self.lastHit=0
        self.numDiffs=0
        self.lastThreeDiffs=[]
        self.freqScore=0  #Score based on frequency
        self.diffScore=0  #Score based on occurances
        self.probScore=0  #Sum/Ave of all scores
        self.meanDistOffset = 0

    def appendHitMatrix(self,draw):
        self.hitMatrix.append(draw)

    def getMeanDist(self,c):
            if c < 6:
                self.meanDistOffset = 15
            else:
                self.meanDistOffset = 7
            self.meanDiv=statistics.mean(self.diffMatrix) - self.meanDistOffset

    def getLastThreeDiffs(self):
        self.numDiffs=len(self.diffMatrix)
        for x in range(self.numDiffs - 3,self.numDiffs):
            self.lastThreeDiffs.append(self.diffMatrix[x])

    def getDiffScore(self):
        # < than mean
        if self.lastThreeDiffs[1] < self.meanDiv:
            self.diffScore -= .1
        if self.lastThreeDiffs[2] < self.meanDiv:
            self.diffScore -= .1
        if self.lastThreeDiffs[1] < self.meanDiv and self.lastThreeDiffs[2] < self.meanDiv:
            self.diffScore -= .1
        # > than mean
        if self.lastThreeDiffs[1] > self.meanDiv:
            self.diffScore += .1
            if(self.lastThreeDiffs[1] - self.meanDiv) > 20 and (self.lastThreeDiffs[1] - self.meanDiv < 40):
                self.diffScore += .1
            elif(self.lastThreeDiffs[1] - self.meanDiv) > 40:
                self.diffScore  += .2
        if self.lastThreeDiffs[2] > self.meanDiv:
            self.diffScore += .1
            if(self.lastThreeDiffs[2] - self.meanDiv) > 20 and (self.lastThreeDiffs[2] - self.meanDiv < 40):
                self.diffScore += .1
            elif(self.lastThreeDiffs[2] - self.meanDiv) > 40:
                self.diffScore  += .2
        if self.lastThreeDiffs[1] > self.meanDiv and self.lastThreeDiffs[2] < self.meanDiv:
            self.diffScore += .1
        self.diffScore=round(self.diffScore,4)

    def totalUpScore(self,ball):
        self.probScore=self.freqScore + self.diffScore + slp.ball[b].probScore

class drawlist:
    def __init__(self):
        self.score=0
        self.payOut=0
        self.listData={}
        self.matches=[]

    def newDraw(self,drawNum,pred,drawn):
        self.matches.append([drawNum,pred,drawn])
        
def file_len(fname): #Get Number of Draws in File
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def showprob(col):
    for x in range(1,47):
        print(str(x) + " " + str(slp.col[col].ball[x].freqScore))
        
def showdiffs(c):
    for c in range(1,7):
        slp.col[c].seeColDiffs()

def showDiffAves():
    for c in range(1,7):
        sumDiffs = 0
        for b in range(1,slp.col[c].numBalls + 1):
           sumDiffs += slp.col[c].ball[b].diffScore
        print("col " + str(c) + " = " + str(sumDiffs))

def scoreDraw(pred,drawn):
        drawHits=0
        megaHit = 0
        payout = 0
        predMega=pred.pop()
        drawnMega=drawn.pop()
        for p in range(0,5):
            if pred[p] in drawn:
                drawHits += 1
        if predMega==drawnMega:megaHit = 1
        if drawHits == 0 and megaHit == 0:payout = 0
        elif drawHits == 1 and megaHit == 0:payout = 0
        elif drawHits == 0 and megaHit == 1:payout = 1
        elif drawHits == 1 and megaHit == 1:payout = 2
        elif drawHits == 2 and megaHit == 0:payout = 0
        elif drawHits == 2 and megaHit == 1:payout = 10
        elif drawHits == 3 and megaHit == 1:payout = 47
        elif drawHits == 4 and megaHit == 0:payout = 89
        elif drawHits == 4 and megaHit == 1:payout = 1050
        elif drawHits == 5 and megaHit == 0:payout = 18000
        else:payout = 1000000
        return payout
    
#####################################
########## END FUNCTIONS ############
#####################################    

slp=matrix()
slpdraws=drawlist()
drawAndDate=[]
charLineData=[]
testLen=100
slp.numDraws=file_len("allnumbers.txt")
slp.lastDraw=slp.firstDraw + slp.numDraws - 1
inFile=open("allnumbers.txt")
outFile=open("results.txt","w")
pred=[2,8,12,22,7,20]
drawn=[9,3,22,12,44,20]
for drawNum in range(slp.firstDraw,slp.lastDraw - testLen + 1): #loop through draws
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    currentBallIndex=0
    for x in range(1,7):  # read one line at time, feed each number into balls
        currentBallIndex=int(charLineData[x])
        slp.col[x].ball[currentBallIndex].appendHitMatrix(drawNumber) #append num to balls Column HitMatrix
        slp.ball[currentBallIndex].appendHitMatrix(drawNumber) #append num to balls Matrix HitMatrix
        slp.col[x].ball[currentBallIndex].hits += 1 #add 1 to ball-column hitlist
        slp.ball[currentBallIndex].hits += 1        #add 1 to ball-matrix hitlist
        if slp.col[x].ball[currentBallIndex].lastHit != 0:
            currentDiffCol=drawNumber -(slp.col[x].ball[currentBallIndex].lastHit) #Current Diff Column-Ball object
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
slp.mostRecentDraw=drawNumber
for c in range(1,7):   #sortingHitsColumn, sort all sortedHits lists in Col objects
    slp.col[c].sortHits()
    slp.sortHits()
for c in range(1,7):
    slp.col[c].getLeastAndMostCommon()
    slp.getLeastAndMostCommon()
    
for c in range(1,7): #Get Last Three Diff Entries
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].getMeanDist(c)
        slp.col[c].ball[b].getLastThreeDiffs()
        if(c == 1):   # do matrix balls only once, no cols
           slp.ball[b].getMeanDist(c)
           slp.ball[b].getLastThreeDiffs()
####Start Scoring Columns and Matrix#####
for c in range(1,7):  #Frequency Scoring
    for b in range(1,slp.col[c].numBalls + 1):
        freqScore=(slp.col[c].ball[b].hits - slp.col[c].leastCommonHits)/(slp.col[c].mostCommonHits - slp.col[c].leastCommonHits)  #i
        slp.col[c].ball[b].freqScore += freqScore
        if c == 1:   #Matrix...no columns
            freqScore=(slp.ball[b].hits - slp.leastCommonHits)/(slp.mostCommonHits - slp.leastCommonHits)  #i
            slp.ball[b].freqScore += freqScore

for c in range(1,7):
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].getDiffScore()
        if c == 1:  #Matrix...no columns
            slp.ball[b].getDiffScore()

for c in range(1,7):
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].totalUpScore(b) #pass ball arg for matrix ball
        if c == 1:  #Matrix...no columns
            slp.ball[b].totalUpScore(b)

slp.getUnsortedScores()
slp.sortScores()
for c in range(1,7):
    slp.col[c].getUnsortedScores()
    slp.col[c].sortScores()
slp.getMostProbable()

#for testNum in range(0,testLen):

for testNum in range(0,testLen):
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    currentBallIndex=0
"""
    for x in range(1,7):  # read one line at time, feed each number into balls
        currentBallIndex=int(charLineData[x])
        slp.col[x].ball[currentBallIndex].appendHitMatrix(drawNumber) #append num to balls Column HitMatrix
        slp.ball[currentBallIndex].appendHitMatrix(drawNumber) #append num to balls Matrix HitMatrix
        slp.col[x].ball[currentBallIndex].hits += 1 #add 1 to ball-column hitlist
        slp.ball[currentBallIndex].hits += 1        #add 1 to ball-matrix hitlist
        if slp.col[x].ball[currentBallIndex].lastHit != 0:
            currentDiffCol=drawNumber -(slp.col[x].ball[currentBallIndex].lastHit) #Current Diff Column-Ball object
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
"""
    #outFile.write(str(drawNumber) + "\n")

#slpdraws.newDraw(drawNumber,pred,drawn)
inFile.close()
outFile.close()
"""
Read line, iterate through it
   load numbers into ball-coll objects
   load numbers into ball-matrix objects
   load draw number into ball-col ojects hit list
   load draw number into ball-matrix hit list
   add 1 to ball-col and ball-matrix hit lists
   Calculate current diff for ball-col and ball-matrix objects
 FC-M737
"""
