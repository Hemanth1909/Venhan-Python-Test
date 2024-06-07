class Employee:
    num_employees = 0

    def __init__(self, name, employee_id):
        self.name = name
        if self.validate_employee_id(employee_id):
            self.employee_id = employee_id
        else:
            raise ValueError("Invalid employee ID format")
        Employee.num_employees += 1

    @classmethod
    def get_num_employees(cls):
        return cls.num_employees

    @staticmethod
    def validate_employee_id(employee_id):
        return employee_id.isdigit()

emp1 = Employee("John Doe", "12345")
emp2 = Employee("Jane Smith", "67890")

print(Employee.get_num_employees())
