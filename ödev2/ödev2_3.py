yazi = ["ahmet", "altı", "yaşında", "zeynep", "dört", "yaşında", "esra", "iki", "yaşında", "ayşe", "bir", "yaşında"]

rakamlar = {
    "sıfır": 0,
    "bir": 1,
    "iki": 2,
    "üç": 3,
    "dört": 4,
    "beş": 5,
    "altı": 6,
    "yedi": 7,
    "sekiz": 8,
    "dokuz": 9
}
kosul = 0
#ilk önce yazı dizisinin elemanlarında gezilir
for i in yazi:
    #elemanın rakamlar sözlüğünde olup olmadığı kontrol edilir
    for j in rakamlar:
        if i == j:
            #eğer rakam varsa sayı yazılır
            print(rakamlar[j], end=" ")
            kosul = 1
            break
        else:
            #eğer rakam yoksa kosul sıfır olarak kalır ve yazi dizinin çıktısının verilmesine devam edilir
            kosul = 0
    if kosul == 1:
        #eğer rakam olduğundan dolayı kosul birse yazi dizininden çıktı verilmez ve döngü devam eder
        continue
    elif kosul == 0:
        print(i, end=" ")

