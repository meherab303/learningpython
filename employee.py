class Employee:
    def __init__(self,name,employee_id,sallary,department):
        self.name=name
        self.employee_id=employee_id
        self.sallary=sallary
        self.department=department
    def display_employee_info(self):
        print(f"Name:{self.name}\nEmployee_id:{self.employee_id}\nSalary:{self.sallary}")    