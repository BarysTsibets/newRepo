class Employee():

    def __init__(self, f_name, l_name, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.increase = 5000


    def descr_employer(self):
        print(f"{self.f_name} {self.l_name} with salary {self.salary}")

    def change_increase(self, new_increase):
        self.increase = new_increase

    def give_raise(self):
        self.salary = self.salary + self.increase
