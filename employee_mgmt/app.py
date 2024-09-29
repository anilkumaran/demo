from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory employee data (replace with a DB in production)
employees = [
    {'id': 1, 'name': 'John Doe', 'role': 'Developer'},
    {'id': 2, 'name': 'Jane Smith', 'role': 'Manager'}
]

@app.route('/')
def index():
    return "Welcome to Employee Management System"

# # Get all employees
# @app.route('/employees', methods=['GET'])
# def get_employees():
#     return jsonify(employees)

# # Get a specific employee by id
# @app.route('/employees/<int:id>', methods=['GET'])
# def get_employee(id):
#     employee = next((emp for emp in employees if emp['id'] == id), None)
#     if employee:
#         return jsonify(employee)
#     return jsonify({'error': 'Employee not found'}), 404

# # Add a new employee
# @app.route('/employees', methods=['POST'])
# def add_employee():
#     new_employee = request.json
#     employees.append(new_employee)
#     return jsonify(new_employee), 201

# # Update an existing employee
# @app.route('/employees/<int:id>', methods=['PUT'])
# def update_employee(id):
#     employee = next((emp for emp in employees if emp['id'] == id), None)
#     if employee:
#         employee.update(request.json)
#         return jsonify(employee)
#     return jsonify({'error': 'Employee not found'}), 404

# # Delete an employee
# @app.route('/employees/<int:id>', methods=['DELETE'])
# def delete_employee(id):
#     global employees
#     employees = [emp for emp in employees if emp['id'] != id]
#     return jsonify({'message': 'Employee deleted successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
