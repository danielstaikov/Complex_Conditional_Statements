city = input()
commission = float(input())
percent = 0
if commission>10000:
    if city == "Sofia":
        percent = 12
    elif city == "Varna":
        percent = 13
    elif city == "Plovdiv":
        percent = 14.5
    else:
        print("error")
elif commission>1000:
    if city == "Sofia":
        percent = 8
    elif city == "Varna":
        percent = 10
    elif city == "Plovdiv":
        percent = 12
    else:
        print("error")
elif commission>500:
    if city == "Sofia":
        percent = 7
    elif city == "Varna":
        percent = 7.5
    elif city == "Plovdiv":
        percent = 8
    else:
        print("error")
elif commission>=0:
    if city == "Sofia":
        percent = 5
    elif city == "Varna":
        percent = 4.5
    elif city == "Plovdiv":
        percent = 5.5
    else:
        print("error")
else:
    print("error")
if percent !=0:
    print('{:0.2f}' .format(commission*percent/100))
