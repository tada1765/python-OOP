# # iheritance 1:
# class Employee:
#     raise_amt = 1.04
    
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

# '''inheritance Employee class '''
# class Developer(Employee):
#     raise_amt = 1.10 # pyhton use this raise_amt rather than raise_amt from Employee.
    
# dev_1 = Developer('wq','toh',50000)
# dev_2 = Developer('test','user',60000)

# # print(dev_1.email)
# # print(dev_2.email)
# # print(help(Developer)) # see the Method resolution order

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# # iheritance 2:
# class Employee:
#     raise_amt = 1.04
    
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'

#     def fullname(self):
#         return '{} {}'.format(self.first,self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)

# class Developer(Employee):
#     raise_amt = 1.10 
#     ''' code too long not easy to maintenance ''' 
#     # def __init__(self, first, last, pay, prog_lang):
#     #     self.first = first
#     #     self.last = last
#     #     self.pay = pay
#     #     self.email = first + '.' + last + '@company.com'
#     #     self.prog_lang = prog_lang
#     # def apply_raise(self):
#     # ... code too long.
#     ''' wat to amintenance, 
#         just inheritance Employee from ablove.
#         modify a litter bit than u have another new class
#         with all function from Employee class.
#     '''
#     def __init__(self, first, last, pay, prog_lang):
#         ''' same for both but diff in: 
#         super().__init__(first, last, pay) #sigle inheritance
#         Employee.__init__(self,first, last, pay) #multi-inheritance
#         '''
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang

# dev_1 = Developer('wq','toh',50000, 'Python')
# dev_2 = Developer('test','user',60000, 'Java')

# print(dev_1.email)
# print(dev_1.prog_lang)


# iheritance 3:
class Employee:
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10 
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
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
            print('-->', emp.fullname())
    

dev_1 = Developer('wq','toh',50000, 'Python')
dev_2 = Developer('test','user',60000, 'Java')

mgr_1 = Manager('Sue','Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# check instance or sub_class:

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
print(isinstance(dev_1, Manager))
print(isinstance(dev_1, Employee))
print(isinstance(dev_1, Developer))
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))