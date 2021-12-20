import random
import datetime

def dateGen(sdate, edate, q):
    templist = []
    for n in range(q):
        randintLogin1 = random.randint(6, 22)
        randintLogin2 = random.randint(10, 58)
        randintLogout1 = random.randint(randintLogin1, 23)
        randintLogout2 = random.randint(randintLogin2, 59)

        randomDate = sdate + (edate - sdate) * random.random()
        randomDate = datetime.datetime.strptime(str(randomDate), '%Y-%m-%d').strftime('%d/%m/%y')
        randomDate = str(randomDate).replace("/",".")
        randomDateLogin = str(randomDate) + " " + str(randintLogin1) + ":" + str(randintLogin2)
        randomDateLogout = str(randomDate) + " " + str(randintLogout1) + ":" + str(randintLogout2)

        templist.append(randomDateLogin)
        templist.append(randomDateLogout)

    finallist = list(sorted(set(templist)))

    return finallist

def sortingList(listD):
    #Nah, too lazy for that stuff
    return listD
