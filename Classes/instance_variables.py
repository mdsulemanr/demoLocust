class Employee:
    pass


#  CLASS OBJECTS
obj1 = Employee()
obj2 = Employee()

# print(obj1)
# print(obj2)

#  INSTANCE VARIABLES
obj1.first_name = 'Muhammad'
obj1.last_name = 'Suleman Rafi'

obj2.first_name = 'Muhammad'
obj2.last_name = 'Usman Rafi'


# print(obj1.first_name)
# print(obj1.last_name)
# print(obj2.first_name)
# print(obj2.last_name)


class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.salary = pay
        self.email = first_name + '.' + last_name + '@company.com'

    def fullname(self):
        return '{} {} got email address: {}'.format(self.first, self.last, self.email)

    def f_string(self):
        return f'{self.first} {self.last} got email address: {self.email}'


obj1_of_employee2 = Employee('Muhammad', 'Suleman Rafi', 200000)
obj2_of_employee2 = Employee('Muhammad', 'Usman Rafi', 300000)

# print(obj1_of_employee2.email)
# print(obj2_of_employee2.salary)
print(obj1_of_employee2.fullname())
print(obj1_of_employee2.f_string())
