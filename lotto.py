import operator
import strformat
import lottoUtils
import matplotlib.pyplot as plt

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
        self.firstDraw=2375
        self.currentDraw=self.firstDraw-1
        self.currentDiffCol=0
        self.currentDiffMat=0
        self.unsortedHits={}
        self.unsortedScores={}
        self.sortedHits={}
        self.diffScoreMult=2 #For Balls Instatinated in Mat
        self.freqScoreMult=1 #For Balls Instatinated in Mat
        self.lastDraw=0
        self.numDraws=0
        self.drawn=[]
        self.predicted=[0,0,0,0,0,0]
        self.mostProbable=[]
        self.winningCombos={0:0,1:0,10:0,11:0,20:0,21:0,30:0,31:0,40:0,41:0,50:0,51:0,6:0}
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
        self.ball[b].freqScore=self.freqScoreMult*(slp.ball[b].hits - self.leastCommonHits)/(self.mostCommonHits-self.leastCommonHits)

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
        for b in range(1,48):
            self.unsortedScores[b]=self.ball[b].probScore

    def totalUpScore(self,b): #Matrix, no cols
        self.ball[b].probScore=self.ball[b].freqScore + (self.ball[b].diffScore)

    def getPredicted(self):
        for c in range(0,6):
            if c < 5:
                if self.col[c+1].sortedScores[-1][0] in self.predicted:
                    if self.col[c+1].sortedScores[-2][0] in self.predicted:
                        if self.col[c+1].sortedScores[-3][0] in self.predicted:
                            self.predicted[c]=self.col[c+1].sortedScores[-4][0]
                        else:
                            self.predicted[c]=self.col[c+1].sortedScores[-3][0]
                    else:
                        self.predicted[c]=self.col[c+1].sortedScores[-2][0]
                else:
                    self.predicted[c]=self.col[c + 1].sortedScores[-1][0]
            else:
                self.predicted[c]=self.col[c + 1].sortedScores[-1][0]
            
        
class col:
    def __init__(self,numBalls):
        self.ball=[0]
        self.numBalls=numBalls
        self.leastCommonBall=0
        self.leastCommonHits=0
        self.mostCommonBall=0
        self.mostCommonHits=0
        self.unsortedHits={}
        self.unsortedScores={}
        self.sortedScores={}
        self.sortedHits={}
        self.diffScoreMult=2 #For Balls Instatinated in Col
        self.freqScoreMult=1 #For Balls Instatinated in Col
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
        self.freqScoreMult=1
        self.meanDiff=0
        self.lastHit=0
        self.lastThreeDiffs=[]
        self.freqScore=0  #Score based on frequency
        self.diffScore=0  #Score based on occurances
        self.probScore=0  #Sum/Ave of all scores
        self.outlier = 150
        self.runningTotal=0
        self.counter=0

    def getMeanDiff(self):
        self.counter=0
        self.runningTotal=0
        for d in self.diffMatrix:
            if d > self.outlier:
                d == self.outlier
            self.counter +=1
            self.runningTotal += d
        self.meanDiff=self.runningTotal/self.counter

    def appendLastDiffs(self,currentDiff):
        if len(self.lastThreeDiffs) == 3:
            del self.lastThreeDiffs[0]
        self.lastThreeDiffs.append(currentDiff)

    def getDiffScore(self,mult):
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
        self.diffScore=(mult * (round(self.diffScore,4)))

    def getFreqScore(self,c):
        self.freqScore=self.freqScoreMult * (self.hits - slp.col[c].leastCommonHits)/(slp.col[c].mostCommonHits-slp.col[c].leastCommonHits)

    def totalUpScore(self,b):  #ball, has cols
        self.probScore=(self.freqScore) + (self.diffScore) + (slp.ball[b].freqScore) + (slp.ball[b].diffScore)        

def file_len(fname): #Get Number of Draws in File
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def scoreDraw(pred,drawn):
        drawHits = 0
        megaHit = False
        payout = 0
        predMega=pred[5]
        drawnMega=drawn[5]
        for p in range(0,5): #Only 0-4...do not do mega
            if drawn[p] in pred:
                drawHits += 1
        if predMega==drawnMega:
            megaHit = True
        if drawHits == 0 and megaHit == False:
            payout = 0
            slp.winningCombos[0] += 1
        elif drawHits == 0 and megaHit == True:
            payout = 1
            slp.winningCombos[1] += 1
        elif drawHits == 1 and megaHit == False:
            payout = 0
            slp.winningCombos[10] += 1
        elif drawHits == 1 and megaHit == True:
            payout = 2
            slp.winningCombos[11] += 1
        elif drawHits == 2 and megaHit == False:
            payout = 0
            slp.winningCombos[20] += 1
        elif drawHits == 2 and megaHit == True:
            payout = 10
            slp.winningCombos[21] += 1
        elif drawHits == 3 and megaHit == False:
            payout = 12
            slp.winningCombos[30] += 1
        elif drawHits == 3 and megaHit == True:
            payout = 47
            slp.winningCombos[31] += 1
        elif drawHits == 4 and megaHit == False:
            payout = 89
            slp.winningCombos[40] += 1
        elif drawHits == 4 and megaHit == True:
            payout = 1050
            slp.winningCombos[41] += 1
        elif drawHits == 5 and megaHit == False:
            payout = 18000
            slp.winningCombos[50] += 1
        else:
            payout = 1000000
            slp.winningCombos[51] += 1
        return payout

def adraw(inList): #Alalyze Final Draw 
    print("Col   Num    LastThree     freq ball    freq mat     diff ball     diff mat")
    for d in range(0,6):
        print(str(d + 1) + "     " + strformat.rjtwo(inList[d]) + "    ", end="")
        print(strformat.rjlist(slp.col[d+1].ball[inList[d]].lastThreeDiffs) + "      ",end="")
        print(strformat.rjnum(slp.col[d+1].ball[inList[d]].freqScore) + "       ",end="")
        print(strformat.rjnum(slp.ball[inList[d]].freqScore) + "         ",end="")
        print(strformat.rjnum(slp.col[d+1].ball[inList[d]].diffScore) + "        ",end="")
        print(strformat.rjnum(slp.ball[inList[d]].diffScore))

        
def printdiffs(c):
    if c == 6:
        for x in range(1,26):
            if x < 10:
                print(" ",end="")
            print(str(x) + "     " + str(slp.col[c].ball[x].diffScore))
    if c == 0:
        for x in range(1,48):
            if x < 10:
                print(" ",end="")
            print(str(x) + "     " + str(slp.ball[x].diffScore))    
    else:
        for x in range(1,48):
            if x < 10:
                print(" ",end="")
            print(str(x) + "     " + str(slp.col[c].ball[x].diffScore))

def graphDist(c,b):
    y1=slp.col[c].ball[b].diffMatrix
    x1=[]
    for x in range(0,len(slp.col[c].ball[b].diffMatrix)):
        x1.append(x)
    plt.plot(x1,y1,label = "Diff Dist", color="red")
    plt.xlabel("Diff Order")
    plt.ylabel("Diff Magnitude")
    plt.title("Diff Plot for Col# " + str(c) + " Ball# " + str(b))
    plt.legend()
    plt.show()

def graphAll(ballNum):
    x=[]
    y=[]
    for n in range(1,7):
        y.append(slp.col[n].ball[ballNum].diffMatrix) #Y axis plot
        x.append([l for l in range(1,len(slp.col[n].ball[ballNum].diffMatrix) + 1)]) #X-axis incrementals
        #print("Column " + str(n))
        #print(x[n-1])
        print(n)
    plt.plot(x[0],y[0],label = "Column 1", color="red")
    plt.plot(x[1],y[1],label = "Column 2", color="orange")
    plt.plot(x[2],y[2],label = "Column 3", color="yellow")
    plt.plot(x[3],y[3],label = "Column 4", color="green")
    plt.plot(x[4],y[4],label = "Column 5", color="blue")
    plt.plot(x[5],y[5],label = "Column 6", color="indigo")
    #plt.plot(x[0],y[0],label = "Column 7", color="violet")
    plt.xlabel("Diff Order")
    plt.ylabel("Diff Magnitude")
    plt.title("Diff Plot for Ball# " + str(ballNum))
    plt.legend()
    plt.show()
   
#####################################
########## END FUNCTIONS ############
#####################################    

slp=matrix()
drawAndDate=[]
charLineData=[]
testLen=200
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
        slp.col[c].ball[b].getFreqScore(c)
        if c == 1:   #Matrix...no columns
            slp.getFreqScore(b)
for c in range(1,7):
    for b in range(1,slp.col[c].numBalls + 1):
        slp.col[c].ball[b].getMeanDiff()
        slp.col[c].ball[b].getDiffScore(slp.col[c].diffScoreMult)
        if c == 1:  #Matrix...no columns
            slp.ball[b].getMeanDiff()
            slp.ball[b].getDiffScore(slp.diffScoreMult)            
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
for postLoop in range(slp.currentDraw,slp.lastDraw):
    rawLineData=inFile.readline().rstrip()
    charLineData=rawLineData.split('          ') #split number fields
    drawAndDate=charLineData[0].split('     ')   #split Draw number and date 
    drawNumber=int(drawAndDate[0])
    slp.currentDraw +=1
    currentBallIndex=0
    slp.drawn=[]
    for x in range(1,7):
        slp.drawn.append(int(charLineData[x]))
        currentBallIndex=int(charLineData[x])
        slp.readInNumber(x,drawNumber,currentBallIndex)
    for c in range(1,7):  #Frequency Scoring
        for b in range(1,slp.col[c].numBalls + 1):
            slp.col[c].ball[b].getFreqScore(c)
            if c == 1:   #Matrix...no columns
                slp.getFreqScore(b)
    for c in range(1,7):
        for b in range(1,slp.col[c].numBalls + 1):
            slp.col[c].ball[b].getMeanDiff()
            slp.col[c].ball[b].getDiffScore(slp.col[c].diffScoreMult)
            if c == 1:  #Matrix...no columns
                slp.ball[b].getMeanDiff()
                slp.ball[b].getDiffScore(slp.diffScoreMult)
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
    print(str(drawNumber) + "   ",end="")
    strformat.printList(slp.drawn)
    print(",",end="")
    strformat.printList(slp.predicted)
    print("   " + str(payout))
    slp.runningPayout += payout
print("**********************")
print("Test Run Summary")
print("**********************")
lottoUtils.winningDraws(slp.winningCombos)
print("**********************")
print("Running Payout=   " + str(slp.runningPayout))
print("**********************")
print("Numbers Drawn Alalysis")
adraw(slp.drawn)
print("**********************")
print("Numbers Predicted Analysis")
adraw(slp.predicted)
inFile.close()
outFile.close()


#Last Line = 3336
#outFile.write(str(drawNumber) + "\n")
#slpdraws.newDraw(drawNumber,pred,drawn)

#self.probScore=self.freqScore + self.diffScore
#print("testthis".rjust(20,'-'))
