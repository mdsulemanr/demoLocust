class Employee:
    #  CLASS VARIABLES
    number_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first = first_name
        self.last = last_name
        self.salary = pay
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.number_of_employees += 1

    def fullname(self):
        return '{} {} got email address: {}'.format(self.first, self.last, self.email)

    def f_string(self):
        return f'{self.first} {self.last} got email address: {self.email}'

    def add_increment(self):
        return self.salary * self.raise_amount


obj1_of_employee2 = Employee('Muhammad', 'Suleman Rafi', 200000)
obj2_of_employee2 = Employee('Muhammad', 'Usman Rafi', 300000)

print(obj1_of_employee2.number_of_employees)
print(obj1_of_employee2.salary)
print(obj1_of_employee2.add_increment())
print(obj1_of_employee2.raise_amount)
print(Employee.raise_amount)  # access class variables
