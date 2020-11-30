import numpy as np
import datetime


class Employee:
    raise_amount = 1.05
    deduction_amount = 0.8
    _employees = []
    _managers = []
    _developers = []

    def __init__(self, first, last, pay=50000):
        self.first = first
        self.last = last
        self.pay = pay

        self._employees.append(self)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def apply_deduction(self):
        self.pay = int(self.pay * self.deduction_amount)
        
    def __repr__(self):
        return "Employee {}, {}, {}".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return "{} - {} - {}".format(self.fullname, self.email, self.pay)


class Developer(Employee):
    raise_amount = 1.5

    def __init__(self, first_name, last_name, Pay, prog_lang):
        super().__init__(first_name, last_name, Pay)
        self.prog_lang = prog_lang
        self._developers.append(self)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        self._managers.append(self)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname, '|', emp.email)


