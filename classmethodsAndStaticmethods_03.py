# # classmethods, change the class variables for all access:
# class Employee:
#     raise_amt = 1.04
#     num_of_emps = 0 # class variable that not whant to be change

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
    
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount

# emp_1 = Employee('wq','toh',50000)
# emp_2 = Employee('test','user',60000)

# '''set_raise_amt func change raise_amt value in whole class '''
# emp_1.set_raise_amt(1.02) # same
# Employee.set_raise_amt(1.03) # same

# print(Employee.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

# # classmethods: 
# class Employee:
#     raise_amt = 1.04
#     num_of_emps = 0 
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.num_of_emps += 1

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
    
#     @classmethod
#     def set_raise_amt(cls, amount):
#         cls.raise_amt = amount

#     ''' pass string to create Employee class '''
#     ''' cls == self but its for class '''
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-') #split string
#         return cls(first, last, pay)

# emp_1 = Employee('wq','toh',50000)
# emp_2 = Employee('test','user',60000)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)
# new_emp_2 = Employee.from_string(emp_str_2)
# new_emp_3 = Employee.from_string(emp_str_3)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# Staticmethods: 
class Employee:
    raise_amt = 1.04
    num_of_emps = 0 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    ''' pass string to create Employee class '''
    ''' cls == self but its for class '''
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-') #split string
        return cls(first, last, pay)

    ''' static method did not take specific instance or class variable '''
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# emp_1 = Employee('wq','toh',50000)
# emp_2 = Employee('test','user',60000)

import datetime
my_date = datetime.date(2019, 10, 12)
print(Employee.is_workday(my_date))