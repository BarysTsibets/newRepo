import unittest
from testProj import Employee

class TestEmployee(unittest.TestCase):
    """Testing class Employee"""

    def test_descr_employer(self):
        """check that 'descr_employer' will be "Barys", "Tsibets", 60000 """
        my_employee = Employee("Barys", "Tsibets", 60000)
        self.assertEqual(my_employee.descr_employer(),"Barys Tsibets with salary 60000" )

    def test_e_name(self):
        x = Employee("bob", "smith" , 10000)
        self.assertEqual(x.e_name(), "bob")


if __name__ == "__main__":
    unittest.main()
