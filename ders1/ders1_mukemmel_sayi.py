def bolenler_bul(x):
    bolenler =[]
    for i in range(1,x//2+1):
        if x % i == 0:
            bolenler.append(i)
    return bolenler
def mukemmel_mi(x,y):
    if sum(x) == y:
        return 1
    else:
        return 0
sinir = int(input("kaca kadar: "))
for i in range(1,sinir):
    if mukemmel_mi(bolenler_bul(i),i)==1:
        print(i)
    else:
        continue