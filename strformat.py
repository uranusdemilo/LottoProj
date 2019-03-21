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

def rjlist(lis):
    outstr=""
    for pos in range(0,3):
        if len(str(lis[pos]))==1:
            outstr += ("  " + str(lis[pos]))
            if(pos < 2):
                outstr += ","
        elif len(str(lis[pos]))==2:
            outstr += (" " + str(lis[pos]))
            if(pos < 2):
                outstr += ","
        else:
            outstr += str(lis[pos])
            if(pos < 2):
                outstr += ","
    return outstr

def rjnum(num):
    outstr=""
    num=round(num,3)
    outstr=str(num)
    if len(outstr)==1:
        outstr += ".000"
    elif len(outstr)==2 or len(outstr)==3:
        outstr += "00"
    elif len(outstr)==4 and outstr[1]==".":
        outstr += "0"
    return outstr

def rjtwo(num):
    outstr=""
    if(num<10):
        outstr=" " + str(num)
    else:
        outstr=str(num)
    return outstr
