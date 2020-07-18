import unittest
from testProj import Employee

class TestEmployee(unittest.TestCase):
    """Testing class Employee"""

    def setUp(self):
        self.objectt = Employee("bob", "smith" , 10000)

    def test_descr_employer(self):
        """check that 'descr_employer' will be "Barys", "Tsibets", 60000 """
        self.assertEqual(self.objectt.descr_employer(),"bob smith with salary 10000")

    def test_change_increase(self):
        """"Check that salary will increase to '7000' """
        self.assertEqual(self.objectt.change_increase(7000), 7000)

    def test_give_raise(self):
        """CHeck that new salary will be 'New salary is 15000'"""
        self.assertEqual(self.objectt.give_raise(),"New salary is 15000" )

    def test_e_name(self):
        self.assertEqual(self.objectt.e_name(), "bob")


if __name__ == "__main__":
    unittest.main()
