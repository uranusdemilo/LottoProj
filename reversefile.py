inFile=open("allnumbers.txt")
outFile=open("reversed.txt","w")
inData=reversed(inFile.readlines())
for outline in inData:
    outFile.write(outline)
inFile.close()
outFile.close()
