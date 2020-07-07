class ProductivitySystem:
    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            result = employee.work(hours)
            print(f"{employee.name}: {result}")
        print("")


class ManagerRole:
    def work(self, hours):
        return f"screams and yells for {hours} hours."


class SecretaryRole:
    def work(self, hours):
        return f"expends {hours} hours doing office paperwork."


class SalesRole:
    def work(self, hours):
        return f"expends {hours} hours on the phone."


class FactoryRole:
    def work(self, hours):
        return f"manufactures gadgets for {hours} hours."


# class TemporarySecretary(Secretary, HourlyEmployee):
#     """
#     MRO = Method Resolution Order is used to check the order of resolution when
#     a class is derived of two or more classes
#     >>> from employees import TemporarySecretary
#     >>> TemporarySecretary.__mro__
#     (<class 'employees.TemporarySecretary'>, \
#      <class 'employees.HourlyEmployee'>, \
#      <class 'employees.Secretary'>, \
#      <class 'employees.SalaryEmployee'>, \
#      <class 'employees.Employee'>, \
#      <class 'object'>)
#     """

#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)
