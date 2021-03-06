import hr
import employees

salary_employee = employees.SalaryEmployee(1, 'Rafael Freitas', 1500)
hourly_employee = employees.HourlyEmployee(2, 'Viviane de Fatima', 40,  15)
commission_employee = employees.CommissionEmployee(3, 'Massahar Nomura', 1000, 250)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee
])

import hr
import employees
import disgruntled

salary_employee = employees.SalaryEmployee(1, 'John Smith', 1500)
hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)
commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
disgruntled_employee = disgruntled.DisgruntledEmployee(20000, 'Anonymous')
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,
    hourly_employee,
    commission_employee,
    disgruntled_employee
])

