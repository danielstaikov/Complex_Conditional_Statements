show = input()
rows = int(input())
columns = int(input())

show_value = 0
if show == "Premiere":
    show_value = 12.00
elif show == "Normal":
    show_value = 7.50
elif show == "Discount":
    show_value = 5.00
else:
    print("Wrong input")

result = rows*columns*show_value
print("{0:.2f} leva".format(result))
