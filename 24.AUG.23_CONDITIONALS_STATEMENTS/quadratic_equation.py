import math

a = int(input())
b = int(input())
c = int(input())
D = (b * b) - (4 * a * c)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('The solution is', x1, x2)
elif D==0:
    x1 = -b/(2*a)
    x2 = x1
    print('The solution is', x1, x2)
elif D < 0:
    print('There are no real roots of this equation')
