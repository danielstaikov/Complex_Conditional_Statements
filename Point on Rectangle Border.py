x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

isXborder = (x==x1 or x==x2) and y>=y1 and y<=y2
isYborder = (y==y1 or y==y2) and x>=x1 and x<=x2
if isXborder or isYborder:
    print("Border")
else:
    print("Inside / Outside")