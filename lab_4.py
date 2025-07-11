

Employee = [{"ID": 1, "Name": "Hisham" , "Job": "Developer", "Salary": 20000},
            {"ID": 2, "Name": "Mohamed", "Job": "Engineer" , "Salary": 18000}]


while True:
    x = input("Select operation: \n 1 for add, 2 for delete, 3 for view  , 4 for break : ")
    if x == "4":
        print("Exiting the program.")
        break
    if x == "1":
        new_employee = {}
        new_employee["ID"] = len(Employee) + 1
        new_employee["Name"] = input("Enter Name: ")
        new_employee["Job"] = input("Enter Job: ")
        new_employee["Salary"] = int(input("Enter Salary: "))
        Employee.append(new_employee)
        print("Employee added successfully.")

    elif x == "2":
        emp_id = int(input("Enter Employee ID to delete: "))
        flag= False
        for emp in Employee:
            if emp["ID"] == emp_id:
                Employee.remove(emp)
                flag = True
                break
        if not flag:
            print("Employee not found.")
        else:
            print("Employee deleted successfully.")

    elif x == "3":
        for emp in Employee:
            print(emp)

    else:
        print("Invalid operation.")