# Manhattan distance between all
# the pairs of given points
# Return the sum of distance
# between all the pair of points.

pointA, pointB = open('./mazeInput.txt').read().split('\n')
pointA, pointB = [x.split(',') for x in [pointA, pointB]]

DX = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
DY = {'L': 0, 'R': 0, 'U': 1, 'D': -1}


def distanceSum(pointA):
    x = 0
    y = 0
    length = 0
    ans = {}

    for cmd in pointA:
        d = cmd[0]
        n = int(cmd[1:])
        assert d in ['L', 'R', 'U', 'D']
        for i in range(n):
            x += DX[d]
            y += DY[d]
            length += 1
            if (x, y) not in ans:
                ans[(x, y)] = length
    return ans


PA = distanceSum(pointA)
PB = distanceSum(pointB)
both = set(PA.keys()) & set(PB.keys())
part1 = min([abs(x) + abs(y) for (x, y) in both])
part2 = min([PA[p] + PB[p] for p in both])

print(part1, part2)
