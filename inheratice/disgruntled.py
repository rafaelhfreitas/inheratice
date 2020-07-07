"""
Ducking type example, because this kind of employee has implementation for interface calculate_payroll
"""

class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 1000000