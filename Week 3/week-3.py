# # One way statement 
# if 2 >= 4:
#     print("Nilai Berhasil")
# print("Program Selesai")


"""
# Two way statement
if 2 > 3:
    print("Nilai pertama lebih besar dari nilai kedua")
else:
    print("Nilai pertama lebih kecil dari nilai kedua")
print("Program Selesai")



nilaiPertama = int(input("Bilangan Pertama: "))
nilaiKedua = int(input("Bilangan Kedua: "))

if nilaiPertama > nilaiKedua:
    print(f"{nilaiPertama} lebih besar dari {nilaiKedua}")
else:
    print(f"{nilaiPertama} lebih kecil dari {nilaiKedua}")

    
checkAngka = int(input("Masukkan Angka: "))

if (checkAngka % 2 == 0) | (checkAngka < 20):
    print(f"{checkAngka} bilangan genap kurang dari 20")
else:
    print(f"{checkAngka} bukang bilangan genap kurang dari 20")


# Multiple way condition

angka = int(input("Masukkan Angka:  "))

if angka > 1000:
    print(f"{angka} lebih besar dari 1000")
elif angka > 100:
    print(f"{angka} lebih besar dari 100")
elif angka > 10:
    print(f"{angka} lebih besar dari 10")
else:
    print("Nilai tidak memenuhi syarat")

# one way statement
if 2 > 3:
    print(True)
print("Program Selesai")


# Two way statement
if 4 > 3:
    print(True)
else:
    print(False)
print("Program Selesai")


# Multipe way statement

nilai = int(input("Masukkan Nilai:"))

if nilai > 80:
    print("Nilai A")
elif nilai> 70:
    print("Nilai B")
else:
    print("Nilai C")


nilai = int(input("Masukkan Nilai: "))
if nilai > 1000:
    print("Nilai lebih dari 1000")
elif nilai > 100:
    print("Nilai lebih dari 100")
elif nilai > 10:
    print("Nilai lebih dari 10")
else:
    print("Nilai tidak memenuhi syarat")


nilai = int(input("Masukkan nilai: "))

if (nilai > 10) | (nilai % 2 == 0):
    print(f"{nilai} lebih besar dari 10 dan bilangan genap")
else:
    print("Bukan lebih dari 10 atau bukan bilangan genap")
"""

namaBulan = input("Masukkan Nama Bulan: ")

jmlHari = 31

if namaBulan == "april" or namaBulan == "juni" or namaBulan == "september" or namaBulan == "november":
    jmlHari = 30
elif namaBulan == "februari":
    jmlHari = "28 atau 29"

print(f"{namaBulan} memiliki jumlah hari {jmlHari}")