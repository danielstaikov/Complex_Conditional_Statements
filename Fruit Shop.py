product = input()#banana / apple / orange / grapefruit / kiwi / pineapple / grapes
dayOfWeek = input()#Monday / Tuesday / Wednesday / Thursday / Friday / Saturday / Sunday
quantity = float(input())
price = 0

isProductValid = product=="banana" or product=="apple" or product=="orange" or\
                product=="grapefruit" or product=="kiwi" or product=="pineapple" or\
                product=="grapes"
isWorkDay = dayOfWeek == "Monday" or dayOfWeek == "Tuesday" or dayOfWeek == "Wednesday" or\
            dayOfWeek == "Thursday" or dayOfWeek == "Friday"
isWeekend = dayOfWeek == "Saturday" or dayOfWeek == "Sunday"
isValidDay =isWorkDay or isWeekend
if not (isProductValid and isValidDay):
    print("Error")
else:
    if isWeekend:
        if product=="banana":
            price = 2.70
        elif product=="apple":
            price = 1.25
        elif product=="orange":
            price = 0.90
        elif product=="grapefruit":
            price = 1.60
        elif product=="kiwi":
            price = 3.00
        elif product=="pineapple":
            price = 5.60
        else:
            price = 4.20
    else:
        if product=="banana":
            price = 2.50
        elif product=="apple":
            price = 1.20
        elif product=="orange":
            price = 0.85
        elif product=="grapefruit":
            price = 1.45
        elif product=="kiwi":
            price = 2.70
        elif product=="pineapple":
            price = 5.50
        else:
            price = 3.85
    print('{:0.2f}' .format(price*quantity))


