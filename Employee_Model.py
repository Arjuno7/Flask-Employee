# from database import db
#
# class EmployeeModel(db.Model):
#     __tablename__ = 'Employees'
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     empname = db.Column(db.String(), unique=True, nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#
#     def __init__(self, empname, age):
#         self.empname = empname
#         self.age = age
#
#     def register_user_if_not_exist(self):
#         db_emp = EmployeeModel.query.filter(EmployeeModel.empname == self.empname).all()
#         if not db_emp:
#             db.session.add(self)
#             db.session.commit()
#         return True
#
#     def __repr__(self):
#         return '<id {}>'.format(self.id)


from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify


db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = 'employees'
    employee_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'employee_id': self.employee_id,
            'name': self.name,
            'age': self.age
        }





#     def __init__(self):
#         self.employees = []
#
#     def add_employee(self, name, age):
#         new_employee = Employee(name=name, age=age)
#         db.session.add(new_employee)
#         db.session.commit()
#
#     def get_employees(self):
#         return [employee.to_dict() for employee in Employee.query.all()]



# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/F_emp'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# employee_service = EmployeeService()
# db.init_app(app)
#
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     return jsonify(employee_service.get_employees())
#
# @app.route('/employees', methods=['POST'])
# def add_employee():
#     data = request.get_json()
#     name = data.get('name')
#     age = data.get('age')
#     employee_service.add_employee(name, age)
#     return "Employee Added Successfully"
#
# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     app.run(host='0.0.0.0', port=5500)



