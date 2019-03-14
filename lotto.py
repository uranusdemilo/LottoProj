import operator
import statistics

class matrix:
    def __init__(self):
        self.col=[0]
        self.ball=[0]
        self.numBalls=47
        self.col.append(col(47)) # create collumn with 47 balls
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(47))
        self.col.append(col(27)) #Create Mega with 27
        self.leastCommonBall=0; self.mostCommonBall=0
        self.leastCommonHits=0; self.mostCommonHits=0
        self.currentDraw=1374
        self.drawn=[]
        self.currentDiffCol=0
        self.currentDiffMat=0
        self.unsortedHits={}
        self.unsortedScores={}
        self.sortedHits={}
        self.firstDraw=1375
        self.lastDraw=0
        self.numDraws=0
        self.meanDist=0
        self.predicted=[]
        self.mostProbable=[]
        self.runningPayout = 0
        for b in range(1,48):
            self.ball.append(lottoBall(b)) #instantiate ball b
        for b in range(1,48):
            self.unsortedHits[b]=0  #create unsortedHits dictionary

    def readInNumber(self,c,drawNumber,currentBallIndex):
        self.col[c].ball[currentBallIndex].hitMatrix.append(drawNumber) #append num to balls Column HitMatrix
        self.ball[currentBallIndex].hitMatrix.append(drawNumber) #append num to balls Matrix HitMatrix
        self.col[c].ball[currentBallIndex].hits += 1 #add 1 to ball-column hitlist
        self.ball[currentBallIndex].hits += 1        #add 1 to ball-matrix hitlist
        if self.col[c].ball[currentBallIndex].lastHit != 0:
            currentDiffCol=drawNumber -(self.col[c].ball[currentBallIndex].lastHit) #Current Diff Column-Ball object
            self.col[c].ball[currentBallIndex].appendLastDiffs(currentDiffCol)
        else:
            currentDiffCol=drawNumber-(self.firstDraw)
            self.col[c].ball[currentBallIndex].appendLastDiffs(currentDiffCol)
        if(c != 6):                                 # col 6 is Mega....don't include in matrix
            if self.ball[currentBallIndex].lastHit !=0:
                currentDiffMat=drawNumber -(self.ball[currentBallIndex].lastHit)
                self.ball[currentBallIndex].appendLastDiffs(currentDiffMat)
            else:
                currentDiffMat=drawNumber-slp.firstDraw
                self.ball[currentBallIndex].appendLastDiffs(currentDiffMat)
            self.ball[currentBallIndex].diffMatrix.append(currentDiffMat)
            self.ball[currentBallIndex].lastHit=drawNumber
        self.col[c].ball[currentBallIndex].diffMatrix.append(currentDiffCol)
        self.col[c].ball[currentBallIndex].lastHit=drawNumber
        self.col[c].unsortedHits[currentBallIndex] += 1
        self.unsortedHits[currentBallIndex] += 1
        self.col[c].sortHits()
        self.col[c].getLeastAndMostCommon()
        if c == 1:
            self.sortHits()
            self.getLeastAndMostCommon()

    def appendHitMatrix(self,drawn):
        self.hitMatrix.append(drawn)

    def getFreqScore(self,b):
        self.ball[b].freqScore=(slp.ball[b].hits - self.leastCommonHits)/(self.mostCommonHits-self.leastCommonHits)

    def sortHits(self):
        self.sortedHits=sorted(self.unsortedHits.items(), key=operator.itemgetter(1))

    def sortScores(self):
        self.sortedScores=sorted(self.unsortedScores.items(), key=operator.itemgetter(1))

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

    def getPredicted(self):
        for c in range(1,7):
            if c < 6:
                self.predicted.append(slp.col[c].sortedScores[46][0])
            else:
                self.predicted.append(slp.col[c].sortedScores[26][0])

        
class col:
    def __init__(self,numBalls):
        self.numBalls=numBalls
        self.ball=[0]
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
    def getFreqScore(self,b):
        self.ball[b].freqScore=(self.ball[b].hits-self.leastCommonHits)/(self.mostCommonHits-self.leastCommonHits)
         
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
        self.meanDiff=0
        self.lastHit=0
        self.numDiffs=0
        self.lastThreeDiffs=[]
        self.freqScore=0  #Score based on frequency
        self.diffScore=0  #Score based on occurances
        self.probScore=0  #Sum/Ave of all scores

    #def getMeanDist(self,c):
    #        if c < 6:
    #            self.meanDistOffset = 15
    #        else:
    #            self.meanDistOffset = 7
    #        self.meanDiff=statistics.mean(self.diffMatrix) - self.meanDistOffset

    def appendLastDiffs(self,currentDiff):
        if len(self.lastThreeDiffs) == 3:
            del self.lastThreeDiffs[0]
        self.lastThreeDiffs.append(currentDiff)

    def getDiffScore(self):
        # < than mean
        self.diffScore=0
        if self.lastThreeDiffs[1] < self.meanDiff:
            self.diffScore -= .1
        if self.lastThreeDiffs[2] < self.meanDiff:
            self.diffScore -= .1
        if self.lastThreeDiffs[1] < self.meanDiff and self.lastThreeDiffs[2] < self.meanDiff:
            self.diffScore -= .1
        # > than mean
        if self.lastThreeDiffs[1] > self.meanDiff:
            self.diffScore += .1
            if(self.lastThreeDiffs[1] - self.meanDiff) > 20 and (self.lastThreeDiffs[1] - self.meanDiff < 40):
                self.diffScore += .1
            elif(self.lastThreeDiffs[1] - self.meanDiff) > 40:
                self.diffScore  += .2
        if self.lastThreeDiffs[2] > self.meanDiff:
            self.diffScore += .1
            if(self.lastThreeDiffs[2] - self.meanDiff) > 20 and (self.lastThreeDiffs[2] - self.meanDiff < 40):
                self.diffScore += .1
            elif(self.lastThreeDiffs[2] - self.meanDiff) > 40:
                self.diffScore  += .2
        if self.lastThreeDiffs[1] > self.meanDiff and self.lastThreeDiffs[2] < self.meanDiff:
            self.diffScore += .1
        self.diffScore=round(self.diffScore,4)

    def totalUpScore(self,ball):
        self.probScore=self.freqScore + self.diffScore + slp.ball[b].probScore

def file_len(fname): #Get Number of Draws in File
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def showprob(c):
    for x in range(1,slp.col[c].numBalls + 1):
        print(str(x) + " " + str(slp.col[c].ball[x].freqScore))
        
#def showdiffs(c):
#    for c in range(1,7):
#        slp.col[c].seeColDiffs()

def showDiffAves():
    for c in range(1,7):
        sumDiffs = 0
        for b in range(1,slp.col[c].numBalls + 1):
           sumDiffs += slp.col[c].ball[b].diffScore
        print("col " + str(c) + " = " + str(sumDiffs))

def printList(list):
    print("[",end="")
    for n in range(0,6):
        if n == 0:
            if list[n] < 10:
                print((" " + str(list[n])),end=",")
            else:
                print((str(list[n])),end=",")
        elif n > 0 and n < 5:
            if list[n] < 10:
                print(("  " + str(list[n])),end=",")
            else:
                print((" " + str(list[n])),end=",")
        elif n == 5:
            if list[n] < 10:
                print(("  " + str(list[n])),end="]")
            else:
                print((" " + str(list[n])),end="]")

def scoreDraw(pred,drawn):
        drawHits = 0
        megaHit = 0
        payout = 0
        predMega=pred[5]
        drawnMega=drawn[5]
        for p in range(0,4): #Only 4...do not do mega
            if pred[p] in drawn:
                drawHits += 1
        if predMega==drawnMega:
            megaHit = 1
        if drawHits == 0 and megaHit == 0:payout = 0
        elif drawHits == 1 and megaHit == 0:payout = 0
        elif drawHits == 0 and megaHit == 1:payout = 1
        elif drawHits == 1 and megaHit == 1:payout = 2
        elif drawHits == 2 and megaHit == 0:payout = 0
        elif drawHits == 2 and megaHit == 1:payout = 10
        elif drawHits == 3 and megaHit == 0:payout = 12
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
drawAndDate=[]
charLineData=[]
testLen=100
slp.numDraws=file_len("allnumbers.txt")
slp.lastDraw=slp.firstDraw + slp.numDraws - 1
inFile=open("allnumbers.txt")
outFile=open("results.txt","w")
for drawNum in range(slp.firstDraw,slp.lastDraw - testLen + 1):
    rawLineData=inFile.readline()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    slp.currentDraw +=1
    currentBallIndex=0
    for c in range(1,7):  # read one line at time, feed each number into balls
        currentBallIndex=int(charLineData[c])
        slp.readInNumber(c,drawNumber,currentBallIndex)

for c in range(1,7):  #Frequency Scoring
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].getFreqScore(b)
        if c == 1:   #Matrix...no columns
            slp.getFreqScore(b)
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

slp.getUnsortedScores()  #Matrix
slp.sortScores()
for c in range(1,7):    #   Columns
    slp.col[c].getUnsortedScores()
    slp.col[c].sortScores()
slp.getPredicted()
print("Last Precalc Draw = " + str(slp.currentDraw))
d=0
for x in range(slp.currentDraw,slp.lastDraw):
    d += 1
for postLoop in range(slp.currentDraw,slp.lastDraw):
    rawLineData=inFile.readline().rstrip()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    slp.currentDraw +=1
    currentBallIndex=0
    slp.drawn=[]
    for x in range(1,7):  # read one line at time, feed each number into balls
        slp.drawn.append(int(charLineData[x]))
        currentBallIndex=int(charLineData[x])
        slp.readInNumber(x,drawNumber,currentBallIndex)
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
    for c in range(1,7):    #   Columns
        slp.col[c].getUnsortedScores()
        slp.col[c].sortScores()
    slp.getUnsortedScores()
    slp.sortScores()
    slp.getPredicted()
    payout=scoreDraw(slp.predicted,slp.drawn)
    printList(slp.drawn)
    printList(slp.predicted)
    print("   " + str(payout))
#    print("   " + str(slp.probScore))
    slp.runningPayout += payout
print("************")
print(slp.runningPayout)
inFile.close()
outFile.close()


#Last Line = 3328
#outFile.write(str(drawNumber) + "\n")
#slpdraws.newDraw(drawNumber,pred,drawn)

#self.probScore=self.freqScore + self.diffScore
#issues - Prob Score way too high!
