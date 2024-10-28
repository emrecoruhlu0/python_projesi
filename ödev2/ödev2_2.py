liste = [1, 2, 3, 3, 4, 6, 8, 9, 8, 1, 2, 5, 4, 3]
uzunluk = len(liste)
i = 0
while i < uzunluk:
    #diziden eleman silmeler olduğu için dizinin uzunluğunu net vermek sıkıntı olduğu için while döngüsü kullanıldı
    sayim = 1
    j = i + 1
    while j < uzunluk:
        #i elemanından sonra dizinin sonuna kadar aynı sayıdan oluğ olmadığı kontrol edilir
        if liste[i] == liste[j]:
            sayim += 1
            #eğer varsa sayim bir arttırılır ve sonra silinir
            liste.pop(j)
            uzunluk -= 1
            #eleman silindiği içinde uzunluk azalır
            #eleman silindiği için aslında j'yi bir arttırmayarak sonraki elemana geçilmiştir
        else:
            #aynı sayıdan bulunamadığı için j bir arttırılarak sonraki elemanları kontrol etmeye devam edilir
            j += 1
    print(f"{liste[i]} sayisi {sayim} kere var")
    i += 1