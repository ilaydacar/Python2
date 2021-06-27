# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 19:50:20 2021

@author: ilayda
"""

print("""**************************
      Alışverişe Hoşgeldiniz..
      Yapılacaklar:
         1)Toplam Ne Kadar Paranız Var
         2)Parayı Hesaba Aktarma
         3)Parayı Çekme
    Çıkmak için '5' e basınız.
***********************************
""")
Toplam_para=200

while True:
    işlem=input("işlem seçiniz:")
    
    if (işlem=="5"):
        print("çıkış başarılı..")
        break
    elif(işlem=="1"):
        print("Toplam paranız {} TL'dir".format(Toplam_para))
    
    elif(işlem=="2"):
        aktarma=int(input("Hesaba Aktarcağınız Miktarı Giriniz."))
        Toplam_para+=aktarma
        
    elif(işlem=="3"):
        aktarma=int(input("Hesaba Aktarcağınız Miktarı Tekrar Giriniz."))
        if(Toplam_para-aktarma<0):
            print("Para Çekme Başarısız.")
        if(Toplam_para-aktarma>0):
            print("Para Çekme Başarılı..")
            
    else:
        print("geçersiz işlem..")