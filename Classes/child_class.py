class Employee:
    #  CLASS VARIABLES
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def f_string(self):
        return f'Employee "{self.first} {self.last}" has email address: {self.email}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def developer_lang(self):
        return f"{self.first} {self.last} is using {self.prog_lang} language."


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees  # containing list of developers objects

    def add_employee(self, emp):  # add developers objects to the list
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):  # remove developers objects from the list
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):  # print developers objects attributes (inherited from class Employee)
        for emp in self.employees:
            print('-->', emp.fullname())
            print('-->', emp.f_string())
            print(f'Using lang: {emp.prog_lang}')
            print('Getting pay: {}'.format(emp.pay))


# Creating Developer Objects
dev1 = Developer('Muhammad', 'Suleman Rafi', 1000, 'Java')
dev2 = Developer('Muhammad', 'Usman Rafi', 1000, 'Python')

#  Make use of dev objects
# print(dev1.email)
# print(dev1.developer_lang())
# print(dev1.pay)
# dev1.apply_raise()
# print(dev1.pay)
# Creating Manager Object
manager_1 = Manager('Rizwan', 'Aslam', 1000000, [dev1])
new_team_lead = Manager('Rafaqat', 'Javed', 4000)
# Make use of Manger Object and play with its employees(developers)
print(manager_1.email)
print(manager_1.employees)
manager_1.print_employee()

# manager_1.add_employee(dev2)
# manager_1.print_employee()
#
# manager_1.remove_employee(dev1)
# manager_1.print_employee()


