#stale
# seee the file program.py


# from hr import PayrollSystem
# from productivity import ProductivitySystem
# from employees import EmployeeDatabase

# productivity_system = ProductivitySystem()
# payroll_system = PayrollSystem()
# employee_database = EmployeeDatabase()
# employees = employee_database.employees
# productivity_system.track(employees, 40)
# payroll_system.calculate_payroll(employees)


from hr import PayrollSystem, HourlyPolicy
from productivity import ProductivitySystem
from employees import EmployeeDatabase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDatabase()
employees = employee_database.employees
manager = employees[0]
manager.payroll = HourlyPolicy(55)

productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)


import json
from employees import EmployeeDatabase


def print_dict(d):
    print(json.dumps(d, indent=2))


for employee in EmployeeDatabase().employees:
    print_dict(employee.to_dict())

