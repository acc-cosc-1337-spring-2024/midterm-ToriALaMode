#write function tests here, don't add input('') statements here!
import unittest
from src.question_a import get_random_number, test_config # unsure why I keep getting error messages for this part
from src.question_b import reverse_string
from src.question_c import prime_number 
from src.question_d import get_tax_assessed, get_assessment_value

#follow this example to add questions b, c, and d for testing including their functions
# from src.question_a.question_a import test_config
# class Test_Config(unittest.TestCase):
#     def test_question_a_config(self):
#         self.assertEqual(True, test_config())
class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    # a) Test the get_random_number to make sure it generates number in the range of 1 to 5.
    def test_get_random_numbers(self):
        random_number = get_random_number()

        self.assertEqual((1 <= random_number <= 5), True)

    # b) Write the test cases with hello world, the return value should be dlrow olleh.
    # The value hello should return olleh    
    def test_reverse_string():
        assert reverse_string("hello world") == "dlrow olleh"
        assert reverse_string("hello") == "olleh"
    test_reverse_string()

    # c) Test the function with values 4 returns False, 5 returns True, and 11 returns True.
    def test_is_prime_values(self):
        self.assertEqual(False, prime_number(4))
        self.assertEqual(True, prime_number(5))
        self.assertEqual(True, prime_number(11))  

    # d) Write test cases for the functions.
    # get_assessment_value with values:
    # 10000 should return 6000
    # 20000 should return 12000
    def test_get_assessment_value_10000(self):
        self.assertEqual(6000, get_assessment_value(10000))
    def test_get_assessment_value_20000(self):
        self.assertEqual(12000, get_assessment_value(20000))
    # get_tax_assessed with values:
    # 6000 should return 43.20
    # 10000 should return 72
    def test_get_tax_assessed_6000(self):
        self.assertEqual(43.20, get_tax_assessed(6000))
    def test_get_tax_assessed_10000(self):
        self.assertEqual(72, get_tax_assessed(10000))