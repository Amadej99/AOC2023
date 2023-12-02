from math import prod
import os
import re

igre = open(os.path.join('./', 'input.txt'))

sum = 0

# limitations = {
#     'red': 12,
#     'green': 13,
#     'blue': 14
# }

for ix, igra in enumerate(igre):
    colors = {
        'red': [int(x) for x in re.findall("(\d+) red", igra)],
        'green': [int(x) for x in re.findall("(\d+) green", igra)],
        'blue': [int(x) for x in re.findall("(\d+) blue", igra)]
    }
    # passes = True
    # for color, limit in limitations.items():
    #     if any(x > limit for x in colors[color]):
    #         passes = False
    
    # sum += ix + 1 if passes else 0

    # print(igra, passes, sum)

    product = 1

    for value in colors.values():
        largest = int(max(value))
        product = product * largest

    sum += product

print(sum)

    
    