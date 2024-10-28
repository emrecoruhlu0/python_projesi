import random


def kb_sirala(dizi):
    sayim = 0
    i = 0
    while sayim < len(dizi) - 1:
        if dizi[i] > dizi[i + 1]:
            dizi[i], dizi[i + 1] = dizi[i + 1], dizi[i]
            sayim = 0
        else:
            sayim += 1
        i += 1
        if i == len(dizi) - 1:
            i = 0
    return dizi


dizi1 = []
dizi2 = []
for i in range(10):
    dizi1.append(random.randint(1, 100))
    dizi2.append(random.randint(1, 100))

dizi1.extend(dizi2)
kb_sirala(dizi1)

print(dizi1)
