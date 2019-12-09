import math
f = open("module.txt", "r")
fuel = 0
sum = 0
for x in f:
    m = int(x)
    fuel = ((m/3)-2)
    roundFuel = math.floor(fuel)
    sum = sum + roundFuel
print(sum)
