# To run tests, navigate to the top-level directory of
# the codebase and run:
#    python -m unittest
import unittest
import unittest.mock as mock
from unittest.mock import mock_open, patch

import cookie_counter


class TestOutput(unittest.TestCase):
    def test_correct_date(self):
        self.assertTrue(cookie_counter.is_valid_date_format("2012-12-12"))
        self.assertTrue(cookie_counter.is_valid_date_format("0101-01-01"))
        self.assertTrue(cookie_counter.is_valid_date_format("9999-10-21"))
    def test_incorrect_date(self):
        self.assertFalse(cookie_counter.is_valid_date_format("2016-1-05"))
        self.assertFalse(cookie_counter.is_valid_date_format("2016-01-5"))
        self.assertFalse(cookie_counter.is_valid_date_format("2016-1-5"))
        self.assertFalse(cookie_counter.is_valid_date_format("16-01-05"))
        self.assertFalse(cookie_counter.is_valid_date_format("2016/01/05"))
        self.assertFalse(cookie_counter.is_valid_date_format(""))
        

if __name__ == "__main__":
    unittest.main()
