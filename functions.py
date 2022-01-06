import random
import datetime

def randomname(names):
    return names[random.randint(0, len(names) - 1)]

def keyfunc(sort):
    return sort[1]

def dataSetGen(q, names):
    datasetraw = []
    dataset = []
    for n in range(q):
        name = randomname(names)

        # Creates Login Event with time delta
        # NAME, DATETIMEOBJEKT( JAHR, MONAT, TAG, STUNDE, MINUTE), EVENT
        login = [name, datetime.datetime(2022, random.randint(1, 12), random.randint(1, 28), random.randint(6, 18), random.randint(1, 59)), 'login']
        date = login[1].date()
        time = login[1].time()
        delta = datetime.timedelta(hours=random.randint(0, 23 - time.hour), minutes=random.randint(0, 59 - time.minute))

        # Copies login event and adding logout event based on delta to prevent logout event happening on next day
        logout = login.copy()
        logout[1] = datetime.datetime.combine(date, time) + delta
        logout[2] = 'logout'
        datasetraw.append(login)
        datasetraw.append(logout)

    for n in range(len(datasetraw)):
        dataset.append(datasetraw[n])

    dataset.sort(key=keyfunc)
    for r in dataset:
        r[1] = r[1].strftime('%d. %m. %Y %H:%M')

    return dataset
