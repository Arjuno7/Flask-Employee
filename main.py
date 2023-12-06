import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify
from service import EmployeeService
from Employee_Model import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/F_emp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

employee_service = EmployeeService()
db.init_app(app)

@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify(employee_service.get_employees())

@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    employee_service.add_employee(name, age)
    return "Employee Added Successfully"

@app.route('/employees/<id>', methods=['GET'])
def get_employee_by_id():
    return jsonify(employee_service.get_employee_by_id(id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5500)








# app = Flask(__name__)
# # app.config.from_object(os.environ['APP_SETTINGS'])
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy()
# from Employee_Model import EmployeeModel
# employee_service = EmployeeService()
#
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     return employee_service.get_employees()
#
#
# @app.route('/employees', methods=['POST'])
# def add_employee():
#     data = request.get_json()
#     name = data.get('name')
#     age = data.get('age')
#     employee = employee_service.add_employee(name, age)
#     return "Employee Added Successfully"
#
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=5500)
