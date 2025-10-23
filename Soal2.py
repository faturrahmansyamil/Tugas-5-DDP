# soal 2
print("program menghitung luas bangun datar")
print("1. persegi")
print("2. lingkaran")
print("3. Segitiga")

hitung = int(input("Memilih program (1/2/3): "))


match hitung:
   case 1:
     sisi = float(input("masukkan panjang sisi: "))
     luas = sisi * sisi
     print(luas)
   case 2:
     r = float(input("masukkan jari-jari lingkaran: "))
     luas = 3.14 * r * r
     print(luas)
   case 3:
     alas = float(input("Masukkan alas segitiga: "))
     tinggi = float(input("masukkan tinggi segitiga: "))
     luas = 0.5 * alas * tinggi
     print(luas)
   case _:
     print("SALAH PILIH!")
