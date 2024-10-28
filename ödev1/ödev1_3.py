def asal_mi(sayi):
    bolen = 2
    if sayi < 2:
        return 0
    while bolen != sayi//2+1:
        if sayi % bolen == 0:
            return 0
        bolen = bolen + 1
    return 1

sayii = int(input("bir sayı giriniz: "))

if asal_mi(sayii) == 1:
    input("sayi asal")
else:
    input("sayi asal degil")
