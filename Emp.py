### Python Project: Employee Management System
# Employee info 

employees = [
    {
        'id': 101,
        'name': 'Hisham Yonis',
        'salary': 75000,
        'password': '1234',
        'days of absence': 5,
    }
]

def display_employee(emp):
    print("ID\tName\t\tSalary\tDays of Absence")
    print(f"{emp['id']}\t{emp['name']}\t\t{emp['salary']}\t{emp['days of absence']}")

option = '1'

while option != '3':
    print("\n\n-----------------------------------\n")
    print("Welcome to Employee Management System")
    print("1. Add Employee")
    print("2. View Employee Details")
    print("3. Exit")
    option = input("Enter your option: ")

    if option == '1':
        Emp_Info = {
            'id': employees[-1]['id'] + 1 if employees else 100,  # Auto-increment ID
            'name': input("Enter Employee Name: "),
            'password': input("Enter Employee Password: "),
            'Department': input("Enter Employee Department: "),
            'salary': float(input("Enter Employee Salary: ")),
            'days of absence': int(input("Enter Employee Days of Absence: "))
        }
        employees.append(Emp_Info)
        print("Employee added successfully!")
        print("Your id is:", Emp_Info['id'])

    elif option == '2':
        emp_id = int(input("Enter Employee ID to view details: "))
        found = False
        for emp in employees:
            if emp['id'] == emp_id:
                emp_password = input("Enter Employee Password: ")
                for i in range(3):
                    if emp_password == emp['password']:
                        break
                    else:
                        print("Incorrect password. Try again.")
                        emp_password = input("Enter Employee Password: ")
                else:
                    print("Access denied. Too many incorrect attempts.")
                    exit()
                found = True
                
                while True:
                    print("\nEmployee Options: \n")
                    emp_option = input(" 1 Display Employee Details \n 2 Calculate Discount \n 3 Calculate Bonus \n 4 Remind Legal Holidays \n 5 exit account \n Enter your option: ")    
                    if emp_option == '5':
                        print("Exiting account.")
                        break
                    if emp_option == '1':
                        display_employee(emp)
                    elif emp_option == '2':
                        emp['salary'] -= emp['salary'] * 0.1
                        print(f"Salary after 0.1 Discount {emp['name']}: {emp['salary']}")
                    elif emp_option == '3':
                        emp['salary'] += emp['salary'] * 0.05
                        print(f"Salary after .05 Bonus for {emp['name']}: {emp['salary']}")
                    elif emp_option == '4':
                        legal_holidays = 10 - emp['days of absence']
                        if legal_holidays < 0:
                            legal_holidays = 0
                        print(f"Legal Holidays for {emp['name']}: {legal_holidays}")
                    


