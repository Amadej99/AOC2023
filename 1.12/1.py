import os

vrstice = open(os.path.join('./', 'input.txt'))

stevila = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

sestevek = 0

for vrstica in vrstice:
    prvostevilo = 0;
    drugostevilo = 0;
    current_str = ''
    for ix, znak in enumerate(vrstica):
        current_str += znak
        if znak.isnumeric():
            prvostevilo = prvostevilo if prvostevilo != 0 else znak
            drugostevilo = znak
            current_str = ''
            continue
        match = next((x for x in stevila.keys() if x in current_str), False)
        if(match):
            prvostevilo = prvostevilo if prvostevilo != 0 else stevila[match]
            drugostevilo = stevila[match]
            current_str = current_str[-1:]

    stevilo = prvostevilo + drugostevilo
    sestevek += int(stevilo)

print(sestevek)