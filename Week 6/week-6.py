# def cetakNama():
#     print("Nama saya adalah John Doe")

# cetakNama()

# def cetakNama2(nama):
#     print(f"Halo nama saya {nama} salam kenal")

# cetakNama2("John Doe")

# def cetakNamaHobi(nama, hobi="tidur"):
#     print(f"Halo nama saya {nama} hobi saya adalah {hobi}")



# def cetakNamaHobi(nama, hobi="tidur"):
#     print(f"Halo nama saya {nama} hobi saya adalah {hobi}")

# cetakNamaHobi("Supri", "Mancing")
# cetakNamaHobi("Robin", "Lari")
# cetakNamaHobi("Diana")

# namaOrang = input("Masukkan nama: ")
# hobiOrang = input("Masukkan hobi: ")

# cetakNamaHobi(namaOrang, hobiOrang)



"""def perkalian(nilai):
    return nilai * 5

print(perkalian(5))
hasil = perkalian(10)
print(hasil)

nilaiAlas = 5
def luasSegitiga(alas, tinggi):
    luas = 1 * alas * tinggi
    return luas

hitungSeigitiga = luasSegitiga(6, 8)
print(hitungSeigitiga)


word = "hello world"
print(word[0])
print(word[0:5])
print(word.count("l"))

num = 0

for i in word:
    if i == 'l':
        num += 1
print(num)

def hitungHurufL(kata):
    num = 0
    for i in kata:
        if i == 'l':
            num += 1
    return num

def hitungHurufCount(kata):
    num = kata.count("d")
    return num
print(hitungHurufL("hello world"))
print(hitungHurufCount("hello world"))
print(hitungHurufCount("hesoyam"))



def greeting():
    print("Hello World")

greeting()


def greeting(fname):
    print(f"Hello World {fname}")

greeting("Supri")


def hobby(name, kendaraan, hobby="adu cupang"):
    print(f"Hello my name is {name} and my hobby is {hobby} my transportation is {kendaraan}")

# hobby("Supri", "Mancing")
# hobby(name="Supra", hobby="Main burung merpati")
# hobby("Samsul")
hobby("Motor", "supri")
hobby(kendaraan="Motor", name="supri")



def hitungSegitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

print(hitungSegitiga(4, 8))
hasiLuasSegitiga = hitungSegitiga(4, 8)
print(hasiLuasSegitiga)
print(hitungSegitiga(alas=10, tinggi=15))



text = "Hello World"
print(text[0])
print(text[2:4])
print(text.count("o"))

hitung = 0
for i in text:
    if i == "o":
        hitung += 1
print(hitung)

def hitungHuruf(kata):
    hitung = 0
    for i in kata:
        if i == "o":
            hitung += 1
    return hitung

print(hitungHuruf("Hello World"))
print(hitungHuruf("hesoyam"))
"""

hello = "hello wOrld"
goodbye = hello.replace("hello", "goodbye")
print(hello)
print(goodbye)
print(hello.upper())
print(hello.lower())
print(hello.capitalize())
print(hello.swapcase())