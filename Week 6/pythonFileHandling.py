# f = open("demofile2.txt","r")
# print(f.read())
# print(f.readline())
# print(f.readline())

# with open("demofile2.txt", "r") as f:
#     print(f.read(10))

# with open("demofile2.txt", "r") as f:
#     # print(f.readline())

# with open("demofile2.txt", "r") as f:
#     for x in f:
#         print(x)


# with open("/home/lutfianto/Documents/Kuliah/Materi/Python/Week 1/demofile2.txt","r") as f:
#     print(f.read())

# f = open("/home/lutfianto/Documents/Kuliah/Materi/Python/Week 1/demofile2.txt","r")
# print(f.read())

# f.close()

# with open ("demofile2.txt", "r") as f:
#     print(f.readline())
#     print(f.readline())

# f = open("demofile2.txt", "r")
# print(f.readline())
# print(f.readline())

# with open ("demofile2.txt", "r") as f:
#     for x in f:
#         print(x)

# f = open("demofile2.txt", "r")
# print(f.readline())
# f.close()

# f.close()
# print(f.tell())

# with open ("demofile2.txt", "a") as f:
#     f.write("\nnew line")
#     print(f.read())

# with open ("demofile2.txt", "r") as f:
#     print(f.read())

# with open ("demofile2.txt", "w") as f:
#     f.write("This new line")

# with open("demofile2.txt", "r") as f:
#     print(f.read())

# f = open("demofile2.txt", "a")
# f.write("\nEleventh Line")
# f.close()

# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()

# f = open("demofile2.txt", "w")
# f.write("This new line")
# f.close()

# f = open("demofile2.txt", "r")
# print(f.read())
# f.close()

# f = open("myfile.txt", "x")

# with open("myfile.txt", "x"):
#     pass
# f = open("myfile.txt", "x")
# f.close()

import os 

# os.remove("myfile.txt")

# if os.path.exists("myfile.txt"):
#     os.remove("myfile.txt")
# else:
#     print("File doesn't exsits")

# os.rmdir("example")

# os.rename("demofile2.txt", "demofile3.txt")

# import shutil

# shutil.rmtree("example")


# with open("demofile3.txt", "r") as file:
#     x = file.readlines()[2:6]
#     for i in x:
#         print(i)


# with open("demofile3.txt","r+") as file:
#     file.write("\n11 Eleventh Line")
#     file.read()

# a_file = open("demofile3.txt", "r+")

# a_file.seek(0, os.SEEK_END)

# a_file.write("New text \n")

# a_file.seek(0, os.SEEK_SET)

# print(a_file.read())


# f = open('demofile3.txt', 'a+')
# file_content = f.read()
# f.write('Hello World')
# f.close()