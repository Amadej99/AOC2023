import os
from collections import defaultdict

srecke = open(os.path.join('./', 'input.txt'))

totalPoints = 0

dodatneSrecke = defaultdict(int)

for stSrecke, srecka in enumerate(srecke):
    points = 0
    srecka = srecka.strip('\n')[8:]
    izzrebane, zmagovalne = srecka.split('|')
    currentZnak = ''
    izzrebanedigit = []
    zmagovalnedigit = []
    for znak in izzrebane:
        if znak.isdigit():
            currentZnak += znak
        elif len(currentZnak) > 0:
            izzrebanedigit.append(int(currentZnak))
            currentZnak = ''

    for ix, znak in enumerate(zmagovalne):
        if znak.isdigit() and ix == len(zmagovalne) - 1:
            currentZnak += znak
            zmagovalnedigit.append(int(currentZnak))
            currentZnak = ''
        elif znak.isdigit():
            currentZnak += znak
        elif len(currentZnak) > 0:
            zmagovalnedigit.append(int(currentZnak))
            currentZnak = ''

    for digit in izzrebanedigit:
        if digit in zmagovalnedigit:
            points += 1
    
    for i in range(1, points + 1):
        dodatneSrecke[stSrecke + i] += 1
    
    for i in range(dodatneSrecke[stSrecke]):
        for i in range(1, points + 1):
            dodatneSrecke[stSrecke + i] += 1

sum = 0

for key, value in dodatneSrecke.items():
    dodatneSrecke[key] = value + 1
    sum += dodatneSrecke[key]
    
print(dodatneSrecke)
print(sum)
    
