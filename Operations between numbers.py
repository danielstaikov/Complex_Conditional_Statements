number1 = int(input())
number2 = int(input())
operation = input()

if operation == "/":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        print(f"{number1} / {number2} = "
              "{:.2f}".format(number1/number2))
elif operation == "%":
    if number2 == 0:
        print(f"Cannot divide {number1} by zero")
    else:
        print(f"{number1} % {number2} = {number1%number2}")
elif operation == "+":
    change = 0
    if (number1+number2)%2==0:
        change = "even"
    else:
        change = "odd"
    print(f"{number1} + {number2} = {number1+number2} - {change}")
elif operation == "-":
    change = 0
    if (number1-number2)%2==0:
        change = "even"
    else:
        change = "odd"
    print(f"{number1} - {number2} = {number1-number2} - {change}")
elif operation == "*":
    change = 0
    if (number1*number2)%2==0:
        change = "even"
    else:
        change = "odd"
    print(f"{number1} * {number2} = {number1*number2} - {change}")
else:
    print("Wrong operation!")
