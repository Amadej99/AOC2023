import os
from collections import defaultdict 
from math import prod

shema = open(os.path.join('./', 'input.txt'))

polje = []

zasedeniSimboli = defaultdict(list)

sum = 0
product = 0


def checkAdjacent(positions, numbers):
    # print(positions)
    x, y = positions[0]
    firstLine = x - 1 if x - 1 >= 0 else x
    lastLine = x + 1 if x + 1 < len(polje) else x
    firstCol = y - 1 if y - 1 >= 0 else y
    y = positions[-1][1]
    lastCol = y + 1 if y + 1 < len(polje[0]) else y

    # print(firstLine, lastLine, firstCol, lastCol)

    for i in range(firstLine, lastLine + 1):
        for j in range(firstCol, lastCol + 1):
            if (i, j) in positions:
                continue

            if polje[i][j] == '*':
                zasedeniSimboli[(i, j)].append(int(numbers))
                return True
    return False


for vrstica in shema:
    polje.append(vrstica.strip('\n'))

for ix, vrstica in enumerate(polje):
    localPositions = []
    localNumbers = ''
    for iy, znak in enumerate(vrstica):
        if znak.isnumeric() and iy == len(vrstica) - 1:
            localPositions.append((ix, iy))
            localNumbers += znak
            if len(localPositions) >= 1 and checkAdjacent(localPositions, localNumbers):
                print(localNumbers)
                sum += int(localNumbers)
            localPositions = []
            localNumbers = ''

        elif znak.isnumeric():
            localPositions.append((ix, iy))
            localNumbers += znak
        else:
            if len(localPositions) >= 1 and checkAdjacent(localPositions, localNumbers):
                sum += int(localNumbers)
            localPositions = []
            localNumbers = ''

for simbol, stevila in zasedeniSimboli.items():
    if len(stevila) > 1:
        product += prod(stevila)

print(sum)
print(product)
