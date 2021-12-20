import random
import datetime

def quantityCheck():
    q = int(input("How much log events to create?\n"))
    if q % 2 == 0:
        return q
    elif q % 2 != 0:
        print("Should be dividable by 2. Duh. But i'll manage.")
        q += 1
        return q
    else:
        print("Something went really bad. Try again.  ¯\_(ツ)_/¯")
        quantityCheck()


def dateGen(sdate, edate, q):
    print("Creating dates.....\n")
    templist = []
    for n in range(q):
        randintLogin1 = random.randint(6, 22)
        randintLogin2 = random.randint(10, 58)
        randintLogout1 = random.randint(randintLogin1, 23)
        randintLogout2 = random.randint(randintLogin2, 59)

        randomDate = sdate + (edate - sdate) * random.random()
        randomDate = datetime.datetime.strptime(str(randomDate), '%Y-%m-%d').strftime('%d.%m.%y')
        randomDateLogin = str(randomDate) + " " + str(randintLogin1) + ":" + str(randintLogin2)
        randomDateLogout = str(randomDate) + " " + str(randintLogout1) + ":" + str(randintLogout2)

        templist.append(randomDateLogin)
        templist.append(randomDateLogout)

    finallist = list(sorted(set(templist)))
    return finallist


def namesEvents(q,names, dates):
    print("Creating dataset.....\n")
    dataset = []
    for i in range(1, q):
        tempname = names[random.randint(0, len(names) - 1)]
        dataset.append(tempname + ";" + dates[i] + ";login")
        dataset.append(tempname + ";" + dates[i] + ";logout")
    return dataset

def shuffle():
    print("Shuffle events.....\n")