class Employee():

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.increase = 5000


    def descr_employer(self):
        return f"{self.f_name} {self.l_name} with salary {self.salary}"

    def change_increase(self, new_increase):
        self.increase = new_increase
        return self.increase

    def give_raise(self):
        self.salary = self.salary + self.increase
        return f"New salary is {self.salary}"

    def e_name(self):
        return self.f_name



