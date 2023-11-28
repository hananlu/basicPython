"""

n = 5               # While
while n > 0:
    n -= 1
    print(n)


x = 30             # While using if else statement
y = x % 2

while y != 1:
    if x > 0:
        print('X is positive number')
    else:
        print("X is negative number")
    x = int(input("Please enter any values: "))
    y = x % 2

for i in range(2,4):  # Nested Loop
    for j in range(1, 6):
        print(f"{i} * {j} = {i*j}")
    print(" ")

rows = 6              # Nested Loop
for i in range(1, rows):
    for j in range(i):
        print(i, end=' ')
    print('')

a = int(input("Input number: "))
while a < 14:
    print(f"a = {a}")
    a += 1

a = 51 
b = 17

iter = 0
while b < a:
    print(f"a = {a}")
    print(f"b = {b}")
    b = b + (a % 2)
    a = a - 1
    iter += 1
print(f"Iter = {iter}") 

for i in range(1, 11, 2):
    print(i)


for i in ("Hello World"):
    print(i)

d = {"foo":1, "bar": 2, "baz":3}

for k in d.values():
    print(k)

num  = int(input("Enter any number: "))
accum = 0
for i in range(1, num+1):
    text = "height for person-" + str(i) + " = "
    price = int(input(text))
    accum += price
print(f"Accumulation: {accum}")
print(f"Average height is {accum / num}")

x = 100
y = 0
z = 0

while x > 50:
    y = 50
    while y > 10 + z:
        z += 1
        y -= 3;
    x -= z
print(f"Nilai {z}")


n = 5               # While using break
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
print("End Loop")


n = 5              # While using continue
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        continue
print("End Loop")

"""
z = 0
for i in range(0, 15):
    print(i, '', end='')
    if i % 3 == 0:
        continue
    z += 1
    print('The value of z is',z)

