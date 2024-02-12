 

class Dog :
    def __init__(self, name , DOB):
        self.name= name
        self.DOB = DOB

    def print_name(self):
        print(self.name)

    def print_age(self):
        print(2024 - self.DOB)


na1  = Dog("TIM" , 2021)
na1.print_name()
na1.print_age()