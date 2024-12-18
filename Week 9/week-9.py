# groupmember = {'m': ['yusuf', 'alex', 'naufal'],
#                'f': ['angel', 'susanti', 'aulia']}

# index_susanti = groupmember['f'].index('susanti')
# print(index_susanti)
# groupmember['f'].insert(index_susanti-1, 'ana')
# print(groupmember['f'])
# index_yusuf = groupmember['m'].index('yusuf')
# groupmember['m'].insert(index_yusuf, 'made')



# bulan = input("Nama bulan: ")
# hari = 31

# if (bulan == "April" or bulan == "June" or bulan == "September" or bulan == "November"):
#     hari = 30
# elif (bulan == "February"):
#     hari = '28 atau 29'
# print(f"{bulan} memiliki {hari} hari")

# for i in range(1, 6):
#     print(i)

# if (3 < 5):
#     print("A")
# else:
#     print("B")

# mahasiswa = {"nim": [11011, 11012], "nama":["joe", "alice"], "nilai":[80, 90]}

# # for value in mahasiswa.values():
# #     print(value)

# for i in mahasiswa:
#     print(mahasiswa[i])

# for key, value in mahasiswa.items():
#     print(value)

# odd = []
# even = []

# for i in range(1, 11):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(odd)
# print(even)

# def hitung_vokal(teks):
#     vokal = "aeiouAEIOU"
#     jumlah = 0

#     for huruf in teks:
#         if huruf in vokal:
#             jumlah += 1

#     return jumlah

# teks = input(" ")
# print("Jumlah huruf vokal:", hitung_vokal(teks))

# user_data = {
#     'user1': {
#         'name': 'Alice',
#         'age': 30,
#         'hobbies': ['reading', 'gaming']
#     },
#     'user2': {
#         'name': 'Bob',
#         'age': 25,
#         'hobbies': ['cooking', 'hiking']
#     }
# }

# user_hobbies = user_data['user1']['hobbies']  # Mengakses list hobbies dari user1
# user_hobbies.append('swimming')  # Menambahkan hobi baru

# print(user_data['user1']['hobbies'])  # Output seharusnya: ['reading', 'gaming', 'swimming']


# my_dict = {'anggur': 1,
#            'belimbing': 2,
#            'cabai': 3}
# new_dict = {}

# for key, value in my_dict.items():
#     new_dict[value] = key
#     if key == 'belimbing':
#         new_dict['duku'] = 4
#         break
# print(new_dict)

# try:
#     print("Masukkan dua bilangan bulat")
#     a = int(input("Bilangan pertama: "))
#     b = int(input("Bilangan kedua: "))
# except ValueError:
#     print("Input yang Anda masukkan bukan bilangan bulat")
# else:
#     hasil = a + b
#     print(f"Hasil penjumlahan {a} dan {b} adalah {hasil}")


# print('it\'s a book')


import math

postiveValue = int(input("Masukkan bilangan positif: "))

try:
    print(f"Akar kuadrat dari {postiveValue} adalah {math.sqrt(postiveValue)}") 
except ValueError:
    print("Bilangan yang Anda masukkan bukan bilangan positif")
    

# namaBulan  = input("Masukkan nama bulan: ")

# hari = 31

# if (namaBulan == "April" or namaBulan == "June" or namaBulan == "September" or namaBulan == "November"):
#     hari = 30
# elif (namaBulan == "February"):
#     hari = "28 atau 29"

# print(f"{namaBulan} memiliki {hari} hari")

# if ('a'=='a'):
#     print("A")
# else:
#     print("B")


# mahasiswa = {"nim": [11011, 11012], "nama":["joe", "alice"], "nilai":[80, 90]}  

# for key, value in mahasiswa.items():
#     print(value)

# odd = []
# even = []

# for i in range(11):
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# print(odd)
# print(even)


# i = [1]
# i.append(2)
# print(i)


# num = [1, 2, 3, 4, 5]
# print(num[6])

# if (5<3):
#     print("false") # True
# else:
#     print("true") # False