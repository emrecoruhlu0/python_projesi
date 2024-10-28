def kok_bulucu(a,b,c):
    delta = b**2 - 4*a*c
    kokler = []
    if delta < 0:
        print("reel kok yok")
    elif delta == 0:
        kokler.append(-b / (2 * a))
    else:
        print("cift katli kökler var")
        kokler.append((-b + delta**0.5) / (2 * a))
        kokler.append((-b - delta**0.5) / (2 * a))
    return kokler

print("denklemin katsayilarini giriniz:\n")
a, b, c = int(input("a=")), int(input("b=")), int(input("c="))

kokler = kok_bulucu(a, b, c)
print(f"Kökler: {kokler}")

