import json
from Employee_Model import Employee, db

class EmployeeService:
    def __init__(self):
        self.employees = []

    def add_employee(self, name, age):
        new_employee = Employee(name=name, age=age)
        db.session.add(new_employee)
        db.session.commit()

    def get_employees(self):
        return [employee.to_dict() for employee in Employee.query.all()]


    def get_employee_by_id(self,id):
        employee=json.load([employee.to_dict() for employee in Employee.query.all()])
        for i in employee:
            if i['employee_id']==id:
                return i





















# class EmployeeService:
#     def __init__(self):
#         self.employees = []
#
#     def add_employee(self, name, age):
#         new_employee = Employee(name, age)
#         self.employees.append(new_employee)
#
#     def get_employees(self):
#         return [employee.to_dict() for employee in self.employees]