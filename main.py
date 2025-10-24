def hello(msg="Hello World !"):
    return msg

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

'''
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

calendar_create_event()
calendar_create_event()
calendar_create_event()
calendar_create_event()
chrono_events()'''