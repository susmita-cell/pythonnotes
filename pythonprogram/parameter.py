class Employee:
    
    def __init__(self, name="Unknown", emp_id=0, salary=0.0, department="General"):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
        self.department = department
        
        print("Employee Created")
        print("Name:", self.name)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
        print("Department:", self.department)
        print("------------------------")

# Passing all parameters
e1 = Employee("Rahul", 101, 25000, "IT")

# Passing only 2 parameters
e2 = Employee("Sita", 102)

# Passing no parameters (default used)
e3 = Employee()