# Electricity-Bill-Management-System
A menu-driven Electricity Bill Management System developed using Python and OOP concepts, featuring CRUD operations, abstraction, inheritance and bill calculation.
# ⚡ Electricity Bill Management System

## 📌 About the Project

The Electricity Bill Management System is a menu-driven Python application developed using Object-Oriented Programming (OOP) concepts.

It helps manage electricity billing records by allowing users to create, view, update and delete bills. It also calculates electricity charges based on the number of units consumed.

## 🚀 Features

- Create new electricity bills.
- View all billing records.
- Update existing billing information.
- Delete billing records.
- Calculate electricity bills based on units consumed.
- Automatically assign Residential or Commercial bill types.
- Prevent duplicate bill IDs.
- Validate electricity units to prevent negative values.
- Display customer details and calculated bill amounts.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Abstract Classes
- Inheritance
- Encapsulation
- CRUD Operations

## 📚 OOP Concepts Implemented

**1. Abstraction**
- Uses the abstract `Bill` class.
- Defines an abstract `calculate()` method.

**2. Inheritance**
- `ResidentialBill` and `CommercialBill` inherit from the `Bill` class.

**3. Encapsulation**
- Stores electricity units in a private attribute `__units`.
- Uses `get_units()` to access the units.

## 💰 Electricity Bill Calculation

The bill amount is calculated according to the following unit-based rates:

| Electricity Units | Rate per Unit |
|---|---:|
| Up to 100 | ₹5 |
| 101–300 | ₹10 |
| 301–500 | ₹15 |
| Above 500 | ₹18 |

**Note:** The applicable rate is multiplied by the total units consumed.

## 📂 Project Structure

```text
Electricity-Bill-Management-System/
│
├── main.py
└── README.md
```

## ⚙️ How to Run the Project

**Step 1:** Install Python 3 on your computer.

**Step 2:** Clone this repository.

```bash
git clone https://github.com/YOUR-USERNAME/Electricity-Bill-Management-System.git
```

**Step 3:** Open the project folder.

```bash
cd Electricity-Bill-Management-System
```

**Step 4:** Run the Python program.

```bash
python main.py
```

## 📋 Application Menu

text
1. Create a Bill
2. Show Bills
3. Update Bills
4. Delete Bills
5. Exit


## ⚠️ Limitations

- Billing records are stored temporarily in a Python dictionary.
- Records are not permanently saved after the program exits.
- The project currently runs through a command-line interface.

## 🎯 Learning Outcomes

- Understanding Python OOP concepts.
- Implementing CRUD operations.
- Working with abstract classes and inheritance.
- Applying input validation.
- Developing menu-driven Python applications.

