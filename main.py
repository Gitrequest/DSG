import datetime
import random
import data
import functions

listN = []
listD = []
listT = []
listE = []
q = 10 #how much data to create
sdate = datetime.date(2022, 1, 1)       #input
edate = datetime.date(2022, 12, 31)     #input

listDTemp = functions.dateGen(sdate, edate, q)
print(str(listDTemp) + " ListDTemp")
#names = da
print(data.dataReaderNames())










#for n in range(q):
#    listD = functions.sortingList(listDTemp)

#    listD.append(testlist[0])
#    listD.append(testlist[1])

#listD1 =
#listD2 =
#listD = list(sorted(set(listD)))



    #print(n)
    #listN.append(random.randint(10, 20))
    #listD.append(functions.dateGen(sdate, edate))
    #listT.append(random.randint(10, 20))
    #listE.append(random.randint(10, 20))


#listD = sorted(set(listD))
#print(listD)
#functions.timeGen(listD)
#for n in range(q):
#    dataset = str(listN[n]) + str(listD[n]) + str(listT[n]) + str(listE[n])
    #print(dataset)


#print(dataset)

#print(testliste)