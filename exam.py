employees = []

while True:
    print("Enter your choice:")
    print("1) Add new employee")
    print("2) Print all employees")
    print("3) Delete by age")
    print("4) Update Salary by name")
    print("5) End the program")
    choice =  int(input("Choice number: "))

    if choice == 1:
        name = input("Enter employee name: ")
        age = int(input("Enter employee age: "))
        salary = float(input("Enter employee salary: "))
        employee = {"name": name, "age": age, "salary": salary}
        employees.append(employee)
        print(f"Employee {name} added successfully.")

    elif choice == 2:
        if not employees:
            print("No employees to display.")
        else:
            for emp in employees:
                print(f"Name: {emp['name']}, Age: {emp['age']}, Salary: {emp['salary']}")

    elif choice == 3:
        age = int(input("Enter the age to delete employees: "))
        employees = [emp for emp in employees if emp['age'] != age]
        print(f"Employees with age {age} deleted.")

    elif choice == 4:
        name = input("Enter the employee name to update salary: ")
        found = False
        for emp in employees:
            if emp['name'] == name:
                new_salary = float(input(f"Enter new salary for {name}: "))
                emp['salary'] = new_salary
                print(f"Salary updated for {name}.")
                found = True
                break
        if not found:
            print(f"Employee named {name} not found.")

    elif choice == 5:
        print("Ending the program.")
        break

    else:
        print("Invalid choice, please try again.")
