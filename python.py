print("Hosgeldiniz!")
isim="ali"
soyisim="can"
print("Ad: ",isim,"\nSoyad: ",soyisim)

rakamalar=[1,2,3,4]
print("rakamlar",rakamalar)
print(type(rakamalar))#<class 'list'>

esyalar=("kalem","masa","kitap")
print("esyalar",esyalar)
print(type(esyalar))#<class 'tuple'>

harfler={"a","b","c"}
print("harfler",harfler)
print(type(harfler))#<class 'set'>

notlar={"Tukce":5,"Almanca":4,"Ingilizce":"muaf"}
print(notlar)
print(type(notlar))#<class 'dict'>

print(len(soyisim))# sayisim kac karakterse onu gösterir.

#Accsess Yöntemleri

print(soyisim[2]) #(n)bir stringin istenilen degerine ulasir

print(soyisim[-1]) #(n) string deki son elemani getirir.

print(soyisim[len(soyisim)-1]) #(n) string deki son elemani getirir.

print(soyisim[-len(soyisim)]) #(c) string deki ilk elemani getirir.

print(soyisim[0:2]) #(ca) bir stringdeki istenilen indexteki karakterleri getirir.

print(soyisim[1:]) #(an) belirtilen index ve sonrasini getirir.
print(soyisim[-3:]) #(an) belirtilen index ve sonrasini getirir.

print(soyisim[:2]) #(ca) belirtilen indexin öncesini getirir.
print(soyisim[:-1]) #(ca) belirtilen indexin öncesini getirir.

print(soyisim[-3:-1]) #(ca) geriden baslayarak da istenilen karakterler yazdirilabilir.

print(soyisim[::2]) #(cn) bir karakter atlayarak bir string'i getirir.




