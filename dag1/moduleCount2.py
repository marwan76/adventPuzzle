import math
f = open("module.txt", "r")
fuel=0
summa=0
for x in f:
    m=int (x)
    while m >=0:
        fuel = ((m/3)-2)
        roundFuel = math.floor(fuel)
        m = roundFuel
        if m>=0:
            summa = summa+m
print (summa)
