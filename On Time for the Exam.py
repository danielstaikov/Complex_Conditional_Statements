hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

exam_time = hour_exam*60 + minute_exam
arrive_time = hour_arrive*60 + minute_arrive

if arrive_time <= exam_time:
    if arrive_time < (exam_time-30):
        print("Early")
        early_time_hour = (exam_time - arrive_time)//60
        early_time_minutes = (exam_time - arrive_time)%60
        if early_time_hour < 1:
            print(f"{early_time_minutes} minutes before the start")
        else:
            print(f"{early_time_hour}:"
                  "{:02d} hours before the start".format(early_time_minutes))
    else:
        print("On time")
        print(f"{exam_time - arrive_time} minutes before the start")
else:
    print("Late")
    late_time_hour = (arrive_time - exam_time)//60
    late_time_minutes = (arrive_time - exam_time)%60
    if late_time_hour<1:
        print(f"{late_time_minutes} minutes after the start")
    else:
        print(f"{late_time_hour}:"
              "{:02d} hours after the start".format(late_time_minutes))
