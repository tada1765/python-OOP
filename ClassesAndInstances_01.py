# # python object-oriented programing

# class Employee:
#     pass

# emp_1 = Employee()
# emp_2 = Employee()

# print(emp_1)
# print(emp_2)
# ''' not benefit using class this way'''
# emp_1.first = 'wq'
# emp_1.last = 'toh'
# emp_1.email = 'wq.toh@company.com'
# emp_1.pay = 50000
# emp_2.first = 'test'
# emp_2.last = 'user'
# emp_2.email = 'test.user@company.com'
# emp_2.pay = 60000

# print(emp_1.email)
# print(emp_2.email)
''' instance variable = variable defined in a class '''
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    ''' may useful when you find the class 
        ceate a method() to print fullname'''
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('wq','toh',50000)
emp_2 = Employee('test','user',60000)

print(emp_1.email)
print(emp_2.email)
''' both do same thing '''
print(emp_1.fullname())
print(Employee.fullname(emp_1))
