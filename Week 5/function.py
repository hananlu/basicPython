# def my_function(fname):
#     print(f"{fname} Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(fname, lname):
#     print(fname + lname)

# my_function("Tobias", "Emil", "linus")
# my_function("Emil")
# my_function("Linus",  " Refsnes")

# def my_function():
#     print("Hello from a function")

# my_function()

# global_var = "New program"

# def local_scope():
#     local_var = "pyhton"
#     print(local_var)

# local_scope()
# print(global_var)
# print(local_var)

# def funct1():
#     local_var = 888
#     print("Nilai ", local_var)

# def funct2():
#     print("Nilai ", local_var)

# funct1()
# funct2()


# def sum_number(*args):
#     result = 0

#     for x in args:
#         result += x

#     return result

# print(sum_number(1, 2, 3, 67))


# def country(name="Indonesia"):
#     print(f"I am from {name}")


# country("Sweden")
# country()

# def food_function(food):
#     for x in food:
#         print(x)

# fruits = ['orange', 'apple', 'grape']
# food = ['cake', 'bread', 'banana']
# animals = ['ant', 'cat', 'dog']

# food_function(animals)


# def persegi_panjang(p, l):
#     return p*l

# print(persegi_panjang(4, 5))

# world = "Hello World"

# print(world.upper())
# print(world.lower())
# print(world.title())
# print(world.capitalize())
# print(world.swapcase())

# def example_function(name):
#     print(f"{name} hello from function")

# example_function("john")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


# x = 5

# def function1():
#     print(f'{x}')

# def function2():
#     global x
#     x = 555
#     print(f"{x}")

# def function3():
#     print(f"{x}")

# function1()
# function2()
# function3()