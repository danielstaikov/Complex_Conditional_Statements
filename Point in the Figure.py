highness = int(input())
x = int(input())
y = int(input())

border1 = 0
inside1 = (x >= 0 and x<= 3*highness) and (y >= 0 and y <= highness)
if inside1:
    border1 = (x==0 or x==3*highness) or (y==0 or y==highness)

border2 = 0
inside2 = (x >= highness and x<= 2*highness) and (y >= highness and y <= 4*highness)
if inside2:
    border2 = (x==highness or x==2*highness) or (y==highness or y==4*highness)

if border1 or border2:
    if y==highness and (x>highness and x<2*highness):
        print("inside")
    else:
        print("border")
elif inside1 or inside2:
    print("inside")
else:
    print("outside")
