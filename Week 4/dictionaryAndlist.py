
"""
a = ['foo', 'bar', 'baz', 'qux']
b = ['foo', 'bar', 'baz', 'qux']

print(a == b)
print(a is a)


a = ["Budi", 10, "Rani", 20]
print(type(a))
print(a[1])

a = [1, 2, 3, 4]
a[1] = 7
print(a)
a.pop()
print(a)
a.pop(0)
print(a)
a.pop(3)
print(a)


a = [1, 3, 4, 5]
b = a

# print(a)
# print(b)

# b[1] = 2

# print(a)
# print(b)

c = a.copy()
print(a)
print(c)

c[1] = 2 
print(a)
print(c)

# a.extend(b)
# print(a)
# b.extend(a)
# print(b)

# a.append(10)
# a.insert(1, 2)
# print(a)



shopping = ["Soda", "Cake", "Fruit", "Biscuit"]
search = "Fruit"

if search in shopping:
    print(shopping.index(search))
else:
    print(-1)


a = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in a:
#     print(f"Index list {a.index(i)} = {i}")

print(a[:])
print(a[4:])
print(a[:3])
print(a[3:5])
print(a[-1])


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# print(a * b)
# print(a * 2)
# print(a + b)
# print(b + 5)
# print(a - b)
# print(a / b)


student = {"id":1107, "name":"dhina", "sex":"f", "age":20, "gpa":3.27}
print(student)
print(student["id"])
print(student.values())


"""
groupMember = {"m":["dedi", "ariel", "adam"], "f":["dini", "rani", "sally"]}
print(groupMember)
print(groupMember["m"])
print(groupMember["m"][0])
""""
groupMember = {"m":"dian", "f": "rachel", "x":["a", "b", "c"]}

for i in groupMember:
    print(groupMember[i])

"""