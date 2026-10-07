def toplama(a, b):
    return a + b


def cikarma(a, b):
    return a - b


def carpma(a, b):
    return a * b


def bolme(a, b):
    if b == 0:
        return "Sıfıra bölünemez!"
    return a / b


islemler = {
    "1": toplama,
    "2": cikarma,
    "3": carpma,
    "4": bolme
}


for i in range(5):

    print("\n--- HESAP MAKİNESİ ---")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")

    secim = input("Seçiminiz: ")

    if secim not in islemler:
        print("Geçersiz seçim!")
        continue

    sayi1 = float(input("Birinci sayı: "))
    sayi2 = float(input("İkinci sayı: "))

    sonuc = islemler[secim](sayi1, sayi2)

    print("Sonuç:", sonuc)
