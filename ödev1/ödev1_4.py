def asal_veya_bolen(sayi):
    bolen = 2
    bolenler = []
    if sayi < 2:
        return 0
    while bolen != sayi//2+1:
        if sayi % bolen == 0:
            bolenler.append(bolen)
        bolen = bolen + 1
    if bolenler == []:
        return 1
    else:
        bolenler.insert(0,1)
        bolenler.append(sayi)
        return bolenler

aralik_ilk, aralik_son = int(input("araligin ilk sayisini girin: ")) , int(input("araligin son sayisini girin: "))

for i in range(aralik_ilk , aralik_son + 1):
    if asal_veya_bolen(i) == 1:
        print(f"{i} sayisi asal")
    else:
        print(f"{i} sayisi asal degil bolenleri: {asal_veya_bolen(i)}")



