listGenap = []
listGanjil = []
for i in range(1, 21):
    if i % 2 == 0:
        listGenap.append(i)
    else:
        listGanjil.append(i)
print(f"List pada bilangan Genap {listGenap}")
print(f"List pada bilangan Ganjil {listGanjil}")
        