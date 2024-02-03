from string import digits, ascii_lowercase, ascii_uppercase, punctuation
from check_self_attributes import *
import unittest


class TestPasswordChecker(unittest.TestCase)
    base_score = 0

    def test_input_exists(self):
        assert self is not None


    def test_is_str(self):
        assert is_str(self)


    def test_input_contains_special(self):
        assert contains_special(self)


    def test_input_contains_upper(self):
        assert contains_upper(self)


    def test_input_contains_lower(self):
        assert contains_lower(self)


    def test_input_contains_number(self):
        assert contains_number(self)


    def test_compute_strength_returns_something(self):
        assert compute_password_strength(self) is not None


    def test_compute_strength_return_type(self):
        assert isinstance(compute_password_strength(self), int)


    def test_contains_upper_increment(self):
        assert compute_password_strength("E") > TestPasswordChecker.base_score


    def test_contains_special_increment(self):
        assert compute_password_strength("/") > TestPasswordChecker.base_score


    def test_contains_lower_increment(self):
        assert compute_password_strength("n") > TestPasswordChecker.base_score


    def test_contains_number_increment(self):
        assert compute_password_strength("7") > TestPasswordChecker.base_score

if __name__ == '__main__':
    unittest.
