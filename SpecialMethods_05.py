''' reference: https://docs.python.org/3/reference/datamodel.html#special-method-names '''

# print(1+2)
# print(int.__add__(1,2))
# print(str.__add__('a','b'))
# print(len('test')) # result = 4
# print('test'.__len__()) # same result = 4
import datetime
print(datetime.__file__) # find the datetime module and study

# class Employee:
#     raise_amt = 1.04

#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last +'@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

#     def __repr__(self):
#         return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

#     def __str__(self):
#         return '{} - {}'.format(self.fullname(),self.email)

# emp_1 = Employee('wq','toh',50000)
# emp_2 = Employee('test', 'Employee', 60000)

# ''' result on print(emp_1) when:
# 1.dont have __repr__ and __str__ 
# result: <__main__.Employee object at 0x02D7BE50>

# 2.only have __repr__
# result: Employee('wq','toh','50000')

# 3.have both __repr__ and __str__
# result: wq toh - wq.toh@email.com
# '''
# print(emp_1)

# # print(repr(emp_1)) # call __repr__ right away
# # print(str(emp_1)) # call __str__ right away
# # print(emp_1.__repr__()) # same
# # print(emp_1.__str__())


class Employee:
    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last +'@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('wq','toh',50000)
emp_2 = Employee('test', 'Employee', 60000)

''' if this one command out the emp_1 + emp_2 is error
def __add__(self, other):
        return self.pay + other.pay
'''
print(emp_1 + emp_2) #50000 + 60000

print(emp_1)
print(len(emp_1))