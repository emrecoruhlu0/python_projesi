kenar1, kenar2, kenar3 = int(input("ilk kenari girin:")) , int(input("ikinci kenari girin:")) , int(input("ucuncu kenari girin:"))

if kenar1 + kenar2 > kenar3 and kenar3 + kenar2 > kenar1 and kenar1 + kenar3 > kenar2:
    if kenar1 == kenar2 == kenar3:
        print("eskenar ucgen")
    elif kenar1 == kenar2 or kenar1 == kenar3 or kenar2 == kenar3:
        print("ikizkenar uzgen")
    else:
        print("cesitkenar ucgen")
else:
    print("ucgen olamaz!")