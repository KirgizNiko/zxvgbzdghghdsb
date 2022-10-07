from profil import Profil
import os
#------------------------------------------------------#
ad = Profil.ad
soyad = Profil.soyad
para = Profil.para
sinif = Profil.sinif
print(Profil.ad)
print(f"""
___________________________________________________
|  [G] - GÖNDER | [D] - DOĞRULA | [K] - KREDİ
|--------------------------------------------------
|////////| {ad}
|/Profil/| {soyad}
|////////| {sinif}                           
|{para}$
|__________________________________________________
""")
response1 = input(">>> ")