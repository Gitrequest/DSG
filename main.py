import datetime
import data
import functions

# function for input: how much data to create
q = functions.quantityCheck()

#setting a default logdate value range
sdate = datetime.date(2021, 10, 1)
edate = datetime.date(2022, 12, 31)

#doing the magic
listDTemp = functions.dateGen(sdate, edate, q)
names = data.dataReaderNames()
dataset = functions.namesEvents(q, names, listDTemp)
data.dataWriterDataset(dataset)
