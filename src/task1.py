import json
from flask import Flask, jsonify, request

# Create Flask app
app = Flask(__name__)

# Sample employee data
employees = [
    {'id': 1, 'name': 'Ashley'},
    {'id': 2, 'name': 'Kate'},
    {'id': 3, 'name': 'Joe'}
]

nextEmployeeId = 4

# Function to get employee by ID
def get_employee(emp_id):
    return next((e for e in employees if e['id'] == emp_id), None)

# Function to validate employee data
def employee_is_valid(employee):
    return 'name' in employee

# -------------------------
# CREATE EMPLOYEE (POST)
# -------------------------
@app.route('/employees', methods=['POST'])
def create_employee():
    global nextEmployeeId

    employee = json.loads(request.data)

    if not employee_is_valid(employee):
        return jsonify({'error': 'Invalid employee properties.'}), 400

    employee['id'] = nextEmployeeId
    nextEmployeeId += 1
    employees.append(employee)

    return '', 201, {'location': f'/employees/{employee["id"]}'}

# -------------------------
# UPDATE EMPLOYEE (PUT)
# -------------------------
@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = get_employee(id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist.'}), 404

    updated_employee = json.loads(request.data)

    if not employee_is_valid(updated_employee):
        return jsonify({'error': 'Invalid employee properties.'}), 400

    employee.update(updated_employee)

    return jsonify(employee)

# -------------------------
# DELETE EMPLOYEE (DELETE)
# -------------------------
@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    global employees

    employee = get_employee(id)

    if employee is None:
        return jsonify({'error': 'Employee does not exist.'}), 404

    employees = [e for e in employees if e['id'] != id]

    return jsonify(employee), 200

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)