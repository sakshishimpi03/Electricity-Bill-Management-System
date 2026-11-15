
from abc import ABC, abstractmethod

class Bill(ABC):
    def __init__(self, id, name, units):
        self.id = id
        self.name = name
        self.__units = units

    def get_units(self):
        return self.__units

    @abstractmethod
    def calculate(self):
        pass


class ResidentialBill(Bill):
    def calculate(self):
        return get_amount(self.get_units())


class CommercialBill(Bill):
    def calculate(self):
        return get_amount(self.get_units())


def get_amount(units):
    if units <= 100:
        return units * 5
    elif units <= 300:
        return units * 10
    elif units <= 500:
        return units * 15
    else:
        return units * 18


bills = {}

def create():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    units = int(input("Enter units: "))

    if units < 0:
        print("Invalid units!")
        return

    if id in bills:
        print("ID already exists!")
        return

    if units <= 300:
        bills[id] = ResidentialBill(id, name, units)
    else:
        bills[id] = CommercialBill(id, name, units)

    print("Bill created!")


def read():
    for id, bill in bills.items():
        print("ID:", bill.id,
              "Name:", bill.name,
              "Units:", bill.get_units(),
              "Bill Type:", type(bill).__name__,
              "Bill Amount: Rs.", bill.calculate())


def update():
    id = int(input("Enter ID to update: "))

    if id in bills:
        name = input("Enter new name: ")
        units = int(input("Enter new units: "))

        if units < 0:
            print("Invalid units!")
            return

        if units <= 300:
            bills[id] = ResidentialBill(id, name, units)
        else:
            bills[id] = CommercialBill(id, name, units)

        print("Bill updated!")
    else:
        print("Bill not found!")


def delete():
    id = int(input("Enter ID to delete: "))

    if id in bills:
        del bills[id]
        print("Bill deleted!")
    else:
        print("Bill not found!")


while True:
    print("\n1. Create a Bill")
    print("2. Show Bills")
    print("3. Update Bills")
    print("4. Delete Bills")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice!")
