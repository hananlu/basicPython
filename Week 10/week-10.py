"""
object = A bundle of related attributes (variables) and methods (functions)
Ex: phone, cup, book
You need a "class" to create an object

class = (blueprint) used to design the structure and layout of an object



class Car:

    # cosnturctor

    def __init__(self, model, year, color, for_sale): #Attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Methods
    def drive(self):
        print(f"You drive the {self.model}")

    def stop(self):
        print(f"You stop the {self.model}")


car1 = Car("Toyota", 2020, "Red", True)
car2 = Car("BMW", 2021, "Black", False)

print(car1.model)
print(car2.model)

car1.drive()



class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def checkBalance(self):
        print(f"Your balance is: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance is: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficient funds !! \nYour balance is: {self.balance}")
        else:
            self.balance -= amount


account1 = BankAccount("John", 666666, 1000)
account1.checkBalance()
print(account1.name)
print(account1.balance)
print(account1.account_number)
account1.deposit(500)
account1.withdraw(2000)



class BankAccount:

    def __init__(self, name, account, balance=0):
        self.name = name
        self.account = account
        self.balance = balance

    def checkBalance(self):
        print(f"Jumlah saldo anda {self.balance}")
    
    def nameAccount(self):
        print(f"Nama rekening anda {self.name}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Jumlah saldo anda {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Saldo anda tidak cukup !! \nJumlah saldo anda {self.balance}")
        else:
            self.balance -= amount
            print(f"Jumlah saldo anda {self.balance}")

user1 = BankAccount("Doe", 666666, 12000)

user1.checkBalance()
user1.nameAccount()
user1.deposit(5000)
user1.withdraw(10000)
user1.withdraw(10000)



class human:

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def showName(self):
        print(f"My name is {self.name}")

class employee(human):
    def __init__(self, job):
        self.job = job

human1 = human("Bob", 29, "Indonesia")

print(human1.name)

"""


class BankAccount:

    def __init__(self, nama, rekening, saldo=0):
        self.nama = nama
        self.rekening = rekening
        self.saldo = saldo

    def checkSaldo(self):
        print(f"Jumlah saldo anda sebesar {self.saldo}")

    def depositSaldo(self, amount):
        self.saldo += amount

    def withdrawSaldo(self, amount):
        if self.saldo < amount:
            print(f"Saldo tidak mencukupi, jumlah saldo anda {self.saldo}")
        else:
            self.saldo -= amount


class Asuransi(BankAccount):


    def accountAsuransi(self):
        print("ini aku untuk asuransi")


asuransi1 = Asuransi("john", 6666, 1000)
print(asuransi1.nama)
asuransi1.accountAsuransi()


# user1 = BankAccount("john", 6666, 1000)
# user1.checkSaldo()
# user1.depositSaldo(5000)
# user1.checkSaldo()
# user1.withdrawSaldo(10000)
# user1.checkSaldo()
# user1 = BankAccount("john", 6666, 1000)
# user2 = BankAccount("Bob", 6661, 2000)
# user3 = BankAccount("Alice", 6662, 100)