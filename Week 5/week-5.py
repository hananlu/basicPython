"""
a = [1, 2, 3, 4, 5]

print(a)
print(type(a))
print(a[3])

a[2] = 6
print(a)
a.pop(3)
print(a)
a.insert(1, 10)
print(a)
a.append(7)
print(a)


a = [1, 2, 3, 4, 5]

for i in a:
    print(i)

nama = ["Andi", "Budi", "Caca", "Deni", "Euis"]


for i in range(0, len(nama)):
    print(f"nama ke {i+1} {nama[i]}")



a = [1, 2, 3, 4, 5]
b = a
print(a)
print(b)
b[0] = 0
print(b)
print(a)

c = [1, 2, 3, 4, 5]
d = c.copy()
print(c)
print(d)
d[0] = 0 
print(d)
print(c)


students = {"id": 1102, "name": "Andi", "age": 21}
students["nama"] = "Samsul"
print(students)
students.pop("nama")
print(students)
students["name"] = "Samsul"
print(students)

a = [1, 2, 3, 4, 5]
print(a[2])
print(a[1:4])
a[2] = 6
print(a)
a.append(7)
print(a)
a.pop()
print(a)
a.pop(1)
print(a)


a = [1, 2, 3, 4, 5]
b = a
# print(a)
# print(b)
b[0] = 7
print(b)
print(a)

c = [6, 7, 8, 9, 10]
d = c.copy()
print(c)
print(d)
d[0] = 11
print(d)
print(c)


umur = [12, "tiga belas", 14, "lima belas"]
# print(umur)

for i in range(len(umur)):
    print(f"data ke{i+1} adalah {umur[i]}")


for i in umur:
    print(i)


student = {"id": 1102, "name": "Andi", "age": 21}
# print(student)
# print(type(student))
print(student)
print(student["name"])
student["name"] = "Budi"
print(student["name"])
print(student)
student["gpa"] = 3.5
print(student)
student.pop("gpa")
print(student)

mahasiswa = {"id": 1102, "name": ["Andi"], "age": 21}

print(mahasiswa["name"].append("Budi"))
print(mahasiswa)
mahasiswa["name"][1] = "Bahtiar"
print(mahasiswa)
"""

mahasiswa = {"id": [1102], "name": ["Andi"], "age": [21]}
print(mahasiswa)
mahasiswa["name"].append("David")
print(mahasiswa)
mahasiswa["name"][1] = "Budi"
print(mahasiswa)
print(mahasiswa.values())