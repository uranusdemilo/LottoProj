import sys
def month(textMonth):
	if textMonth == "Jan":
		return "01-"
	elif textMonth == "Feb":
		return "02-"
	elif textMonth == "Mar":
                return "03-"
	elif textMonth == "Apr":
                return "04-"
	elif textMonth == "May":
                return "05-"
	elif textMonth == "Jun":
		return "06-"
	elif textMonth == "Jul":
		return "07-"
	elif textMonth == "Aug":
		return "08-"
	elif textMonth == "Sep":
		return "09-"
	elif textMonth == "Oct":
                return "10-"
	elif textMonth == "Nov":
                return "11-"
	elif textMonth == "Dec":
                return "12-"
	else:
		return "error"

def formatday(rawday):
	if(rawday in singledays):
                rawday = rawday.replace(",","")
        	return ("0" +rawday +"-")
        else:
                return (rawday +"-")
        print dateparts[2]

singledays = ["1","2","3","4","5","6","7","8","9"]

lottofile = open("copypasteupdate.txt","r")
lottosorted = open("lottoupdate.txt","w")
line = ['junk1','junk2']
n = 0
arrayoflines = []
while line:
	line = lottofile.readline()
	line = line.replace(',','')
	line = line.replace('\t','')
	line = line.replace(' -','')
	lineparts = line.split(' ',5)
	# lineparts(0) = Month  3) = Draw
	#           1) = Day   4) = Draw Numbers
	#			2) = Year 5) = Mega
	if len(lineparts) > 1:
		num_month = month(lineparts[0])
		linetoprint = ''
		if(num_month in singledays):
			linetoprint = '0' + num_month
		else:
			linetoprint = num_month
		if(lineparts[1] in singledays):
			linetoprint += '0' + lineparts[1]
		else:
			linetoprint += lineparts[1]
		linetoprint += '-' + lineparts[2] + ' ' + lineparts[3] + ' '
		linetoprint += lineparts[4][0:2] + ' ' + lineparts[4][2:4] + ' ' + lineparts[4][4:6] + ' '
		linetoprint += lineparts[4][6:8] + ' ' + lineparts[4][8:10] + ' ' + lineparts[4][10:12]
		if(lineparts[5].strip() in singledays):
			linetoprint += '0' + lineparts[5]
		else:
			linetoprint += lineparts[5]
		print linetoprint.strip()
		arrayoflines.append(linetoprint)
numlines = len(arrayoflines)
lineon = numlines - 1
for output in range(0,numlines - 1):
	lottosorted.write(arrayoflines[lineon])
	lineon -= 1
