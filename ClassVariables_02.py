''' class variable = variable shared among all instences of class '''
# # class variables 1:
# class Employee:
#     ''' class variables '''
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#         ''' error not found raise_amount:   
#                 to access raise_amount needed 
#                 through the class itself or 
#                 instance of the class.
#         example:
#         self.pay = int(self.pay * raise_amount) error
#         use this: 
#         self.pay = int(self.pay * Employee.raise_amount) class itself
#         or:
#         self.pay = int(self.pay * self.raise_amount) instance of the class '''
# emp_1 = Employee('wq','toh',50000)
# emp_2 = Employee('test','user',60000)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# ''' way to access and see class variable raise_amount '''
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# print(emp_1.__dict__) # not found raise_amount
# print(Employee.__dict__) # found raise_amount


# # class variables 2:
# class Employee:
#     raise_amount = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)

# emp_1 = Employee('wq','toh',50000)
# emp_2 = Employee('test','user',60000)

# ''' change raise_amount value '''
# Employee.raise_amount = 1.05 # change all
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# Employee.raise_amount = 1.04 # change back 1.04
# emp_1.raise_amount = 1.05 # change only emp_1
# print(emp_1.__dict__) # now raise_amount founded
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# class variables 3:
class Employee:
    raise_amount = 1.04
    num_of_emps = 0 # class variable that not whant to be change

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

print(Employee.num_of_emps)

emp_1 = Employee('wq','toh',50000)
emp_2 = Employee('test','user',60000)

print(Employee.num_of_emps)

''' 
Summary:
    to access class variables only 
    through the class itself or 
    instance of the class.
    example:
    self.pay = int(self.pay * raise_amount) error
    use this: 
    self.pay = int(self.pay * Employee.raise_amount) class itself
    or:
    self.pay = int(self.pay * self.raise_amount) instance of the class
'''
