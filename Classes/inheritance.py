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

    def apply_raise(self):
        self.salary = self.salary * self.raise_amount


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first_name, last_name, pay, prog_lang):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

    def developer_lang(self):
        return f"{self.first} {self.last} is using {self.prog_lang} language."


# print(help(Developer))
dev1 = Employee('Muhammad', 'Suleman Rafi', 1000)
dev2 = Developer('Muhammad', 'Usman Rafi', 1000, 'Python')

print(dev1.salary)
dev1.apply_raise()
print(dev1.salary)

print(dev2.prog_lang)
print(dev2.developer_lang())
