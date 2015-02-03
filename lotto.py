class lottocol(object):
	def __init__(self,columnNum,numBalls):
		self.columnNum = columnNum
		self.numBalls = numBalls
		
	def printnum(self):
		sys.stdout.write('Column Number: ')
		print self.columnNum
import sys		
infile = open("lottosorted.txt","r")
line = 'junk'
while line:
	line = infile.readline()
	print line
	
col1 = lottocol(1,40)

col1.printnum()
	