from datetime import datetime
def conflict_time(event1,event2):
    startTime1=datetime.strptime(event1[0],"%H:%M")
    endTime1=datetime.strptime(event1[1],"%H:%M")
    startTime2=datetime.strptime(event2[0],"%H:%M")
    endTime2=datetime.strptime(event2[1],"%H:%M")
    if(startTime2<startTime1 and endTime2<startTime1 or startTime2>endTime1 and endTime2>endTime1):
        print("True")
        return 
    else:
        print("False")
        return 
conflict_time(["01:15","02:00"],["02:05","03:00"])