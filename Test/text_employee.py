import unittest
from employee import Employee
from unittest.mock import patch


class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")
        self.emp1 = Employee("Corey", "Schafer", 5000)
        self.emp2 = Employee("Soe", "Smith", 6000)

    def tearDown(self):
        print("tearDown")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp1.email, "Corey.Schafer@gmail.com")
        self.emp1.first = "John"
        self.assertEqual(self.emp1.email, "John.Schafer@gmail.com")

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule("May")
            mocked_get.assert_called_with("http://company.com/Schafer/May")
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.emp2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June")
            self.assertEqual(schedule, "Bad Response!")


if __name__ == '__main__':
    # run all of us tests.
    # each function is a test.
    unittest.main()
