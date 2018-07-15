budget = float(input())
season = input()
destination = 0
type_vacation = 0
spend_money = 0
if budget > 1000:
    destination = "Europe"
    type_vacation = "Hotel"
    spend_money = 0.9*budget
elif budget>100:
    destination = "Balkans"
    if season == "summer":
        type_vacation = "Camp"
        spend_money = 0.4*budget
    else:
        type_vacation = "Hotel"
        spend_money = 0.8*budget
else:
    destination = "Bulgaria"
    if season == "summer":
        type_vacation = "Camp"
        spend_money = 0.3*budget
    else:
        type_vacation = "Hotel"
        spend_money = 0.7*budget
print(f"Somewhere in {destination}")
print(f"{type_vacation} - "+"{:.2f}".format(spend_money))
