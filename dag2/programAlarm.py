"""
pos = position
"""
pos = [int(x) for x in open ('./dag2/intInput.txt').read().split(',')]

pos[1]=12
pos[2]=2

intRead=0
while True:
    operationCode=pos[intRead]
    i1, i2, i3 = pos[intRead+1], pos[intRead+2],pos[intRead+3]
    if operationCode ==1:
        pos[i3] = pos[i1]+pos[i2]
    elif operationCode==2:
        pos[i3] = pos[i1]*pos[i2]
    else:
        assert operationCode == 99
        break
    intRead +=4
print(pos)