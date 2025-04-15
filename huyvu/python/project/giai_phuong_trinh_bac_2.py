import math
print("hay nhap lan luot cac he so a,b,c: ")

a = int(input())
b = int(input())
c = int(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh co vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x = -c/b
        print("x = " + str(x))
else:
    delta = (b**2) - (4*a*c)
    if delta > 0:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    elif delta == 0:
        x = -b/2*a
        print("x = " + str(x))
    else:
        print("phuong trinh vo nghiem")
        