# While Loop
"""
a = 1
jumlah = 0

while a <= 5:
    jumlah += a
    print(f"nilai ke {a} jumlah {jumlah}")
    a = a + 1


a = 1
jumlah = 0

while a <= 5:
    jumlah += a
    a = a + 1
print(f"Total jumlah nilai adalah {jumlah}")


nilaiPertama = int(input("Bilangan Pertama:"))
nilaiTerakhir = int(input("Bilangan Terakhir:")) 

while nilaiPertama <= nilaiTerakhir:
    if nilaiPertama % 2 == 0:
        print(nilaiPertama)
    nilaiPertama += 1


# For Loop

for i in range(1, 6, 3):
    print(i)

nilaiAwal = int(input("Nilai Awal: "))
nilaiAkhir = int(input("Nilai Akhir: "))

for i in range(nilaiAwal, nilaiAkhir+1):
    print(i)
print("Program Selesai")

nilaiAwal = int(input("Nilai Awal: "))
nilaiAkhir = int(input("Nilai Akhir: "))

for i in range(nilaiAwal, nilaiAkhir+1):
    print(i)
    if i == 3:
        break
print("Program Selesai")

nilaiAwal = int(input("Nilai Awal: "))
nilaiAkhir = int(input("Nilai Akhir: "))

for i in range(nilaiAwal, nilaiAkhir+1):
    print(i)
    if i == 3:
        continue
print("Program Selesai")


# Nested Loop

for i in range(1, 6):
    for j in range(1, 6):
        if (i == 3) and (j == 3):
            continue
        print(f" {i} + {j} = {i+j}")


# while loops
a = 1

while a < 5:
    print(a)
    a += 2


a = 1
jumlah = 0

while a <= 5:
    jumlah += a
    print(f"nilai ke {a} jumlah {jumlah}")
    a += 1
print(f"Total jumlah nilai adalah {jumlah}")


# For loops
numA = int(input("Bilangan Pertama: "))
numB = int(input("Bilangan Terakhir: "))

for i in range(numA, numB+1):
    if i % 2 == 0:
        print(i)



# Nested Loop

# for i in range(1,6):
#     for j in range(3, 6):
#         print(f"{i} {j}")

# Break statement

for i in range(1, 10):
    if i == 8:
        break
    print(i)
print("Program selesai")
"""
# Continue statement


for i in range(1, 11):
    for j in range(2, 11):
        if (j == 5):
            break
    print(i)
    






