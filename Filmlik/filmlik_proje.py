from filmlik import *

print("""
********************************

Filmlik Uygulamasına Hoşgeldin

********************************
""")

print("""
Yapabileceğiniz İşlemler

1) Filmlikteki filmleri göster

2) Film ekle

3) İsme göre film sorgula

4) Yıla göre film sorgula

5) İsim değiştir

6) Film sil

Çıkmak için 'q' yaz.

""")

filmlik=Filmlik()

while True:
    işlem=input("Yapmak istediğiniz işlem: ")
    
    if işlem=="q":
        break
    elif işlem=="1":
        filmlik.filmleri_göster()
    elif işlem=="2":
        a=input("İsim: ")
        b=input("Tür: ")
        c=int(input("Yıl: "))
        d=float(input("Puan: "))
        
        film=Film(a,b,c,d)
        filmlik.film_ekle(film)
    elif işlem=="3":
        a=input("Aramak istediğin filmin adı: ")
        filmlik.isme_göre(a)
    elif işlem=="4":
        a=int(input("Aramak istediğin yıl: "))
        filmlik.yıla_göre(a)
    elif işlem=="5":
        a=input("Değiştirmek istediğin filmin şu anki adı: ")
        b=input("Yeni adı: ")
        filmlik.isim_değiş(a,b)
    elif işlem=="6":
        a=input("Silmek istediğin filmin adı: ")
        b=input("Emin misin? E/H ")
        if b=="E":
            filmlik.isimle_sil(a)
    else:
        print("Geçersiz işlem")



