import data
import functions

q = int(input("How much log events to create?\n"))
data.dataWriterDataset(functions.dataSetGen(q, data.dataReaderNames()))
