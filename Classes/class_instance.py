class Employee:
    # class_variables which we want to keep same/un-changed for all instances
    company_name = 'Arbisoft Pakistan'

    # congrats_msg = "Congrats! (), with role as: (), employee of Company: (), " \
    #                "you've been given annual increment of ()"

    # INSTANCE variables which we can change or keep unique instance to instance
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.min_raise_amount = 0.05
        self.congrats_msg = "Congrats! (), with role as: (), employee of Company: (), " \
                            "you've been given annual increment of ()"

    def increment_msg(self):
        return f"Congrats! {self.name}, with role as: {self.designation}, working in: {Employee.company_name}," \
               f" you've been given annual increment of {self.min_raise_amount}"

    # def increment_msg(self):
    #     return self.congrats_msg.format(self.name, self.designation, self.company_name, self.min_raise_amount)


employee1 = Employee('Muhammad Suleman Rafi', 'Sr SQA')
employee1.min_raise_amount = 0.5
print(employee1.increment_msg())

employee2 = Employee('Mr. A', 'SQA')
employee2.company_name = "Arbisoft USA"
employee2.min_raise_amount = 0.4
print(employee2.increment_msg())

employee3 = Employee('Mr. B', 'TL')
employee3.company_name = "Arbisoft USA"
print(employee3.increment_msg())
