"""
pos = position
pos[1]=noun
pos[2]=verb
"""
readList = [int(x) for x in open('./adventPuzzle/dag2/intInput.txt').read().split(',')]
# which pair of inputs results in optOutput
pos = 0
for noun in range(100):
    for verb in range(100):
        pos = [x for x in readList]
        
        pos[1] = noun
        pos[2] = verb

        intRead = 0
        while True:
            operationCode = pos[intRead]
            i1, i2, i3 = pos[intRead+1], pos[intRead+2], pos[intRead+3]
            if operationCode == 1:
                pos[i3] = pos[i1]+pos[i2]
            elif operationCode == 2:
                pos[i3] = pos[i1]*pos[i2]
            else:
                assert operationCode == 99
                break
            intRead += 4
        if pos[0] == 19690720:
            print(noun, verb)
print(pos)
