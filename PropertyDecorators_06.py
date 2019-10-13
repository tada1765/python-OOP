# class Employee:
#     def __init__(self, first , last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# emp_1 = Employee('John', 'Smith')
# emp_1.first = 'Jim' #change name
# ''' name change but email name not update
#     fullname() have update tought.
# '''
# print(emp_1.first)
# print(emp_1.email) 
# print(emp_1.fullname())

# # solution use Getters:
# class Employee:
#     def __init__(self, first , last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first,self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

# emp_1 = Employee('John', 'Smith')
# emp_1.first = 'Jim' #change name

# print(emp_1.first)
# ''' result not have @property:
#     print(emp_1.email) => <__main__.Employee object at 0x02DABD10>>
#     print(emp_1.email()) => Jim.Smith@email.com
#     result have @property on top of email method:
#     print(emp_1.email()) => error
#     print(emp_1.email) => Jim.Smith@email.com

#     we dont want to change our way of access code
#     when we modify some funct. just add @property
#     we can use access method like an attribute like 
#     perviously do. 
# '''
# print(emp_1.email)
# print(emp_1.fullname) # same go to fullname method

# # Setters:
# class Employee:
#     def __init__(self, first , last):
#         self.first = first
#         self.last = last

#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first,self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     @fullname.setter
#     def fullname(self, name):
#         first, last = name.split(' ')
#         self.first = first
#         self.last = last

# emp_1 = Employee('John', 'Smith')
# # emp_1.first = 'Jim' 
# emp_1.fullname = 'wq toh' # error before use setter

# print(emp_1.first)
# print(emp_1.email)
# print(emp_1.fullname) 

# Deleter:
class Employee:
    def __init__(self, first , last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('John', 'Smith')

emp_1.fullname = 'wq toh' # error before use setter

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname) 

del emp_1.fullname # delete
print(emp_1.first)
