budget = float(input())
category = input()
people = int(input())

transport_costs = 0
if people >= 50:
    transport_costs = 0.25*budget
elif people >= 25:
    transport_costs = 0.4*budget
elif people >= 10:
    transport_costs = 0.5*budget
elif people >= 5:
    transport_costs = 0.6*budget
elif people >= 1:
    transport_costs = 0.75*budget
else:
    print("Wrong input")
ticket = 0
if category == "Normal":
    ticket = 249.99
elif category == "VIP":
    ticket = 499.99
else:
    print("Wrong category")
result = budget - (transport_costs +people*ticket)
if result >= 0:
    print("Yes! You have {:0.2f} leva left.".format(result))
else:
    print("Not enough money! You need {:0.2f} leva.".format(abs(result)))
