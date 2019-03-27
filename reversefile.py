#This file reverses the order of lines in the file so that the script can
#access the draws from older to newer.  Download the DownloadAllNumbers.txt
#from the California Lottery site, and open it with a text editor.  Remove
#the top five lines of the file.  Run this script, and it will dump the
#file into "reversed.txt".  Use the startWrite parameter to indicate how
#many of the oldest lines in the file to skip.
inFile=open("DownloadAllNumbers.txt")
outFile=open("reversed.txt","w")
inData=reversed(inFile.readlines())
linePos=0
startWrite=1000
for outline in inData:
    linePos+=1
    if linePos > startWrite:
        outFile.write(outline)
inFile.close()
outFile.close()
