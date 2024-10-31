## Yerel Değişkenler (Local Variables)
def fonksiyon():
    x = 10  # Yerel değişken
    print("Fonksiyon içindeki x:", x)

fonksiyon()
print("Fonksiyon dışındaki x:", "x")  # Bu satır hata verecektir çünkü x yerel bir değişken.

##  Global Değişkenler (Global veritables)
x = 10  # Global değişken

def fonksiyon():
    print("Fonksiyon içindeki x:", x)

fonksiyon()
print("Fonksiyon dışındaki x:", x)  # Global değişken her yerden erişilebilir.

## Global Anahtar Kelimesi ile Değişkenin Değiştirilmesi
x = 10  # Global değişken

def fonksiyon():
    global x
    x = 20  # Global değişkenin değerini değiştiriyoruz
    print("Fonksiyon içindeki x:", x)

fonksiyon()
print("Fonksiyon dışındaki x:", x)  # Global değişken değişmiş olacak.

##Yerel ve Global Değişkenlerin Aynı İsme Sahip Olması
x = 10  # Global değişken

def fonksiyon():
    x = 20  # Yerel değişken
    print("Fonksiyon içindeki x (yerel):", x)

fonksiyon()
print("Fonksiyon dışındaki x (global):", x)  # Global değişken hala aynı kalır.

## dictionaries
# Bir sözlük tanımlayalım
ogrenci = {
    "isim": "Ali",
    "yas": 21,
    "bolum": "Bilgisayar Mühendisliği"
}

# Sözlükteki verilere anahtarlar ile erişelim
print(ogrenci["isim"])  # Çıktı: Erdinç 
print(ogrenci["yas"])   # Çıktı: 24
print(ogrenci["bolum"]) # Çıktı: Bilgisayar Mühendisliği

## get() Metodu ile Değer Erişimi //Bu metodu NYP de sık olarak kullandık.
notu = ogrenci.get("not", "Bilgi yok")  # Anahtar varsa değerini döner, yoksa 'Bilgi yok' döner
print(notu)

adres = ogrenci.get("adres", "Adres bulunamadı")  # Anahtar yok, bu yüzden varsayılan değer döner
print(adres)

