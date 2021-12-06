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

soyisim="ozgurluk"

print(soyisim[1:6:2]) #(zul) 1. indexten 6. indexe kadar 1 yaz 1 atla

print(soyisim[:]) #string'in tamamini yazdirir.

#Integer

sayi1=3
print(type(sayi1)) #<class 'int'>

sayi2=3.5
print(type(sayi2)) #<class 'float'>

sayi3=1j
print(type(sayi3)) #<class 'float'>

x=input("ilk sayiyi giriniz: ") #5
y=input("ikinci sayiyi giriniz: ") #8
print("toplam: ",x+y) #toplam:  58
print("toplam: ",int(x)+int(y)) #toplam:  13

print(soyisim*5) #ozgurlukozgurlukozgurlukozgurlukozgurluk










