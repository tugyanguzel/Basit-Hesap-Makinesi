print("-"*40)
giriş = """
(1) topla
(2) çıkar
(3) çarp
(4) böl
(5) kare alma
(6) mod alma 
(q) çıkış
"""
print(giriş)
print("-"*40)

anahtar = 1

while anahtar == 1:
    secim = input("Yapmak istediğiniz işlemin numarasını girin : ")

    if secim == "q":
        print("çıkılıyor...")
        break

    elif secim == "1":
        sayi1 = int(input("Lütfen bir sayı giriniz:"))
        sayi2 = int(input("Lütfen bir sayı girirniz:"))
        sonuc = sayi1 + sayi2
        print("Sonuç:" ,sonuc)
#Çıkarma işlemi
    elif secim == "2":
        sayi1 = int(input("Lütfen bir sayı giriniz:"))
        sayi2 = int(input("Lütfen bir sayı girirniz:"))
        sonuc = sayi1 - sayi2
        print("Sonuç:" ,sonuc)
#Bölme işlemi 
    elif secim == "3":
        sayi1 = int(input("Lütfen bir sayı giriniz:"))
        sayi2 = int(input("Lütfen bir sayı girirniz:"))
        sonuc = sayi1 / sayi2
        print("Sonuç:" ,sonuc)
#Çarpma işlemi 
    elif secim == "4":
        sayi1 = int(input("Lütfen bir sayı giriniz:"))
        sayi2 = int(input("Lütfen bir sayı girirniz:"))
        sonuc = sayi1 * sayi2
        print("Sonuç:" ,sonuc)
    elif secim == "5":
        sayi1 = int(input("Lütfen bir sayı giriniz:"))
        sonuc = sayi1 ** 2
        print("Sonuç:" ,sonuc)
    elif secim == "6":
        sayi1 = int(input("Lütfen bir sayı giriniz:"))
        sayi2 = int(input("Lütfen bir sayı giriniz:"))
        sonuc = sayi1 % sayi2
        print("Sonuç:" ,sonuc)
        
    else:
        print("Yanlış giriş.")
        print("Aşağıdaki seçeneklerden birini giriniz:", giriş)