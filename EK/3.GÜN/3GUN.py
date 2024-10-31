## Temel Fonksiyon Örneği:
def selam_ver(isim):
    print(f"Merhaba, {isim}!")

selam_ver("Ahmet")

##Toplama Fonksiyonu:
def topla(a, b):
    return a + b

sonuc = topla(10, 20)
print(f"Toplam: {sonuc}")

##Varsayılan Parametreli Fonksiyon:
def bilgileri_yazdir(isim, yas=18):
    print(f"İsim: {isim}, Yaş: {yas}")

bilgileri_yazdir("Ali")
bilgileri_yazdir("Ayşe", 25)

##Birden Fazla Değer Döndüren Fonksiyon:
def dikdortgen_alan_ve_cevre(uzunluk, genislik):
    alan = uzunluk * genislik
    cevre = 2 * (uzunluk + genislik)
    return alan, cevre

alan, cevre = dikdortgen_alan_ve_cevre(5, 10)
print(f"Alan: {alan}, Çevre: {cevre}")

## Proje
def toplama(a, b):
    return a + b

def cikarma(a, b):
    return a - b

def carpma(a, b):
    return a * b

def bolme(a, b):
    if b == 0:
        return "Bölme işleminde payda 0 olamaz."
    return a / b

def hesap_makinesi():
    print("İşlem Seçiniz:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    
    secim = input("Seçiminizi yapın (1/2/3/4): ")
    
    if secim in ['1', '2', '3', '4']:
        sayi1 = float(input("Birinci sayıyı girin: "))
        sayi2 = float(input("İkinci sayıyı girin: "))
        
        if secim == '1':
            print(f"Sonuç: {toplama(sayi1, sayi2)}")
        elif secim == '2':
            print(f"Sonuç: {cikarma(sayi1, sayi2)}")
        elif secim == '3':
            print(f"Sonuç: {carpma(sayi1, sayi2)}")
        elif secim == '4':
            print(f"Sonuç: {bolme(sayi1, sayi2)}")
    else:
        print("Geçersiz seçim.")

# Hesap makinesi fonksiyonunu çalıştıralım
hesap_makinesi()


