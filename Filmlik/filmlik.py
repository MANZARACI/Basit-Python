import sqlite3

class Film():

    def __init__(self,isim,tür,yıl,puan):
        self.isim=isim
        self.tür=tür
        self.yıl=yıl
        self.puan=puan

    def __str__(self):
        return (f"Filmin adı: {self.isim}\nTür: {self.tür}\nYıl: {self.yıl}\nPuan: {self.puan}\n")

class Filmlik():

    def __init__(self):
        self.bağlan()
    
    def bağlan(self):
        self.con=sqlite3.connect("filmlik.db")
        self.cursor=self.con.cursor()

        self.cursor.execute("Create table if not exists filmler (İsim TEXT,Tür TEXT,Yıl INT,Puan FLOAT)")
        self.con.commit()
    
    def bağlantı_kes(self):
        self.con.close()

    def film_ekle(self,Film):
        sorgu="Insert into filmler Values (?,?,?,?)"
        self.cursor.execute(sorgu,(Film.isim,Film.tür,Film.yıl,Film.puan))
        self.con.commit()
    
    def filmleri_göster(self):
        sorgu="Select * from filmler"
        self.cursor.execute(sorgu)
        filmler=self.cursor.fetchall()

        if (len(filmler)==0):
            print("Filmlikde film bulunamadı...")
        else:
            for i in filmler:
                film=Film(i[0],i[1],i[2],i[3])
                print(film)
    
    def yıla_göre(self,yıl):
        sorgu="Select * from filmler where Yıl=?"
        self.cursor.execute(sorgu,(yıl,))
        filmler=self.cursor.fetchall()

        if (len(filmler)==0):
            print("Aradığınız yılda bir film bulunamadı...")
        else:
            for i in filmler:
                film=Film(i[0],i[1],i[2],i[3])
                print(film)

    def isme_göre(self,isim):
        sorgu="Select * from filmler where İsim=?"
        self.cursor.execute(sorgu,(isim,))
        filmler=self.cursor.fetchall()
        
        if (len(filmler)==0):
            print("Aradığınız isimde bir film bulunamadı...")
        else:
            film=Film(filmler[0][0],filmler[0][1],filmler[0][2],filmler[0][3])
            print(film)
    
    def isim_değiş(self,eski,yeni):
        sorgu="Update filmler set İsim=? where İsim=?"
        self.cursor.execute(sorgu,(yeni,eski))
        self.con.commit()
    
    def isimle_sil(self,isim):
        self.cursor.execute("Delete from filmler where İsim=?",(isim,))
        self.con.commit()