##Dışardan alınan Proje örneği

# Öğrenci bilgilerini ve notlarını tutan bir sistem

# Ders notlarını kaydetme fonksiyonu
def ders_notlari_gir():
    dersler = {}
    while True:
        ders_adi = input("Ders adı (çıkmak için 'q' ya basın): ")
        if ders_adi == 'q':
            break
        notu = float(input(f"{ders_adi} dersinin notunu girin: "))
        dersler[ders_adi] = notu
    return dersler

# Not ortalaması hesaplama fonksiyonu
def ortalama_hesapla(dersler):
    toplam = sum(dersler.values())
    ortalama = toplam / len(dersler)
    return ortalama

# Geçti mi kaldı mı fonksiyonu
def basari_durumu(ortalama):
    if ortalama >= 60:
        return "Geçti"
    else:
        return "Kaldı"

# Ana fonksiyon
def ogrenci_not_sistemi():
    print("Öğrenci Not Sistemine Hoş Geldiniz!")

    ad = input("Öğrencinin adı: ")
    soyad = input("Öğrencinin soyadı: ")
    
    dersler = ders_notlari_gir()  # Ders notlarını girme

    if len(dersler) == 0:
        print("Hiç ders notu girilmedi!")
        return

    ortalama = ortalama_hesapla(dersler)  # Not ortalaması hesaplama
    durum = basari_durumu(ortalama)  # Başarı durumu belirleme

    print(f"\nÖğrenci: {ad} {soyad}")
    print(f"Ortalamanız: {ortalama:.2f}")
    print(f"Sonuç: {durum}")

# Programı çalıştırma
ogrenci_not_sistemi()