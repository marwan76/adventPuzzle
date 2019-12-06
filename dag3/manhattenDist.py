# Manhattan distance between all
# the pairs of given points
# Return the sum of distance
# between all the pair of points.

A,B = open('./mazeInput.txt').read().split('\n')
A,B = [x.split(',') for x in [A,B]]

DX ={'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY ={'L': 0, 'R': 0, 'U': 1, 'D': -1}
def distancesum(A):
    x=0
    y=0
    ans = set()

    for cmd in A:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U','D']
        for i in range(n):
            x += DX[d]
            y += DY[d]
            ans.add((x,y))
    return ans

PA = distancesum(A)
PB = distancesum(B)
both = PA&PB
ans = min(abs(x) + abs(y) for (x,y) in both)
print(ans)