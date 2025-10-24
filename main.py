def hello(msg="Hello World !"):
    return msg

from datetime import datetime
T1 = 0
list_of_events = []

def calendar_create_event():
    t=0
    n=0
    t = input("combien de seconde depuis le timestamp ?\n")
    n = input("un nom stp\n")
    date = (T1,int(t),n)
    list_of_events.append(date)
    return date


def events():
    for i in list_of_events :
        print(i)
    return list_of_events


def chrono_events():
    list_of_events.sort(key=lambda x: x[1]) #on dit de se baser sur list_of_events[1] pour utilisr le .sort()
    for i in list_of_events :
        print(i)
    return list_of_events

def first_element():
    return list_of_events[0]

def next_event():
    # Récupère la date et l'heure actuelles
    now = datetime.now()
    # Crée un objet datetime correspondant au début de la journée (00:00:00)
    start_of_day = datetime(now.year, now.month, now.day, 0, 0, 0)
    # Calcule la différence
    delta = now - start_of_day
    # Convertit en secondes
    seconds_since_midnight = int(delta.total_seconds())

    list_of_events.sort(key=lambda x: x[1])
    for i in list_of_events :
        if int(i[1])>seconds_since_midnight :
            return i
    return 0


calendar_create_event()
calendar_create_event()
calendar_create_event()
calendar_create_event()
print(next_event())