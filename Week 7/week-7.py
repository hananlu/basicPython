import os

# f = open("exampleFile.txt", "r")
# # for i in f:
# #     print(f.readline())
# f.close()


# with open("exampleFile.txt", "w+") as f:
#     f.write("Hello world")

# os.remove("exampleFile.txt")

# if os.path.exists("exampleFile.txt"):
#     os.remove("exampleFile.txt")
# else:
#     print("The file does not exist")

# with open("exampleFileBackup.txt", "r+") as f:
#     f.read()
#     f.write("Hello my name is John")

# f = open("exampleFileBackup.txt", "r")
# print(f.read())
# print(f.read(10))
# print(f.readline())
# print(f.readline())

# for i in f:
#     print(f.readline())
# f.close()

# f = open("exampleFileBackup.txt", "a")
# f.write("\nHello my name is John")
# f.close()
# f = open("exampleFileBackup.txt", "w")
# f.write("My name is John i'm coming from the United States")
# f.close()

# if os.path.exists("exampleFileBackup.txt"):
#     os.remove("exampleFileBackup.txt")
# else:
#     print("The file does not exist")

open = open("exampleFileBackup.txt", "r")
print(open.read())
open.close()