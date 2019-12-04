import math
f = open("module.txt", "r")
fuel=0
summa=0
for x in f:
    m=int (x)
    fuel = ((m/3)-2)
    roundFuel = math.floor(fuel)
    summa = summa + roundFuel
print(summa)
