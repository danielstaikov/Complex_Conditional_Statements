month = input()
accommodation = int(input())

apartment = 0
studio = 0
reduction_apartment = 1
reduction_studio = 1
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if accommodation > 14:
        reduction_apartment = 0.9
        reduction_studio = 0.7
    elif accommodation > 7:
        reduction_studio = 0.95
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if accommodation > 14:
        reduction_apartment = 0.9
        reduction_studio = 0.8
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if accommodation > 14:
        reduction_apartment = 0.9
else:
    print("Hotel is closed!")
print("Apartment: {:0.2f} lv.".format(accommodation*apartment*reduction_apartment))
print("Studio: {:0.2f} lv.".format(accommodation*studio*reduction_studio))
