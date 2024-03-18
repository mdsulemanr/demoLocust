class Addition:

    # parameterized constructor
    def __init__(self, f, s, z):
        self.multiply_answer = None
        self.sum_answer = None
        self.first = f
        self.second = s
        self.third = z

    def calculate(self):
        self.sum_answer = self.first + self.second + self.third

    def multiply_num(self):
        self.multiply_answer = self.first * self.second * self.third

    def display(self):
        print("First number = " + str(self.first))
        print("Second number = " + str(self.second))
        print("Third number = " + str(self.third))
        print("Addition of three numbers = " + str(self.sum_answer))
        print("Multiplication of three numbers = " + str(self.multiply_answer))


first_object = Addition(1, 2, 3)
second_object = Addition(10, 20, 30)
first_object.calculate()
second_object.calculate()
first_object.multiply_num()
second_object.multiply_num()
first_object.display()
second_object.display()

# creating object of the class
# # this will invoke parameterized constructor
# # obj1 = Addition(1, 2, 3)
# #
# # # creating second object of same class
# # obj2 = Addition(10, 20, 30)
#
# # perform Addition on obj1
# Addition(1, 2, 4).calculate()
#
# # perform Addition on obj2
# Addition(10, 20, 40).calculate()
#
# Addition(1, 2, 4).multiply_num()
# Addition(10, 20, 40).multiply_num()
#
# # display result of obj1
# Addition(1, 2, 4).display()
#
# # display result of obj2
# Addition(10, 20, 40).display()
