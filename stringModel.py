import string

name="tavsan"

#slice

print(name[slice(1,4)]) #avs parca olarak istenilen index arasini alir.

parca=slice(1,4) #tanimlama yaparak da kullanilabilir.
print(name[parca]) #avs

#büyük harf yapma

print(name.upper()) #TAVSAN

#kücük harf yapma

name2=name.upper() #TAVSAN
print(name2) ##TAVSAN
print(name2.lower()) #tavsan

#bas ve sondaki bosluklari silme

kelime="   kahraman   "
print(len(kelime)) # 14

print(len(kelime.strip())) #8

#stringi ayirma (her zaman bir liste getirir)

kelime=kelime.strip()
print(kelime) #kahraman

print(kelime.split("r")) #['kah', 'aman']
print(kelime.split("a"))










