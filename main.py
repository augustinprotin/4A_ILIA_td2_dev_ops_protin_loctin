def hello(msg="Hello World !"):
    return msg
T1 = 0
list_of_events = []

def calendar_create_event():
    t = input("combien de seconde depuis le timestamp ?\n")
    n = input("un nom stp\n")
    date = (T1,int(t),n)
    list_of_events.append(date)
    return date


def events():
    for i in list_of_events :
        print(i)
    return list_of_events

calendar_create_event()
calendar_create_event()
events()