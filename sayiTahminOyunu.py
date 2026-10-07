import random

sayi = random.randint(1, 10)

print("Sayı Tahmin Oyununa Hoş Geldin!")
print("1 ile 10 arasında bir sayı tuttum.")

while True:
    tahmin = int(input("Tahminin: "))

    if tahmin < sayi:
        print("Daha büyük bir sayı denemelisin!")
    elif tahmin > sayi:
        print("Daha küçük bir sayı denemelisin!")
    else:
        print("Tebrikler!")
        break
