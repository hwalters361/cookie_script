# To run tests, navigate to the top-level directory of
# the codebase and run:
#    python -m unittest
import unittest
import unittest.mock
from unittest.mock import mock_open, patch
import cookie_counter


class TestMostUsedCookies(unittest.TestCase):
    mock_file_content = """cookie,timestamp
AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
"""
    @patch("builtins.open", new_callable=mock_open, read_data=mock_file_content)
    def test_example_input1(self, mock_file):
        # Check the first example in the problem statement
        file_path = "fake_file.csv"
        date = "2018-12-09"
        expected_result = "AtY0laUfhglK3lC7\n"
        result = cookie_counter.most_used_cookies(file_path, date)
        self.assertEqual(result, expected_result)
        
    @patch("builtins.open", new_callable=mock_open, read_data=mock_file_content)
    def test_example_input2(self, mock_file):
        # Check the second example in the problem statement
        file_path = "fake_file.csv"
        date = "2018-12-08"

        result = cookie_counter.most_used_cookies(file_path, date)
        self.assertEqual(result.count("\n"), 3) #should be three newlines (one after each cookie)
        
        expected_result_set = {"SAZuXPGUrfbcn5UA","4sMM2LxV07bPJzwf","fbcn5UAVanZf6UtG"}
        # check if all members in the expected result are in the result
        for item in result.split("\n"):
            if bool(item.strip()):
                self.assertTrue(item in expected_result_set)
                expected_result_set.remove(item)
        
        # check that result has covered every expected result (should be empty if we got every one)
        self.assertEqual(len(expected_result_set), 0)
        
        
    @patch("builtins.open", new_callable=mock_open, read_data="""cookie,timestamp
cookie1,2023-01-01T14:19:00+00:00
cookie2,2023-01-01T14:19:00+00:00
cookie3,2023-01-01T14:19:00+00:00
cookie1,2023-01-01T14:20:00+00:00""")
    def test_one_cookie_result(self, mock_file):
        file_path = "fake_file.csv"
        date = "2023-01-01"
        result = cookie_counter.most_used_cookies(file_path, date)
        self.assertEqual(result.count("\n"), 1) #should be one newline
        expected_result = "cookie1\n"
        self.assertEqual(result, expected_result)
        
    @patch("builtins.open", new_callable=mock_open, read_data="""cookie,timestamp
cookie1,2023-01-01T14:19:00+00:00
cookie2,2023-01-01T14:19:00+00:00
cookie3,2023-01-01T14:19:00+00:00""")
    def test_multiple_cookie_result(self, mock_file):
        file_path = "fake_file.csv"
        date = "2023-01-01"
        result = cookie_counter.most_used_cookies(file_path, date)
        self.assertEqual(result.count("\n"), 3) #should be three newlines (one after each cookie)
        
        expected_result_set = {"cookie1","cookie2","cookie3"}
        # check if all members in the expected result are in the result
        for item in result.split("\n"):
            if bool(item.strip()):
                self.assertTrue(item in expected_result_set)
                expected_result_set.remove(item)
        
        # check that result has covered every expected result (should be empty if we got every one)
        self.assertEqual(len(expected_result_set), 0)
                
    @patch("builtins.open", new_callable=mock_open, read_data="""cookie,timestamp
cookie1,2023-01-01T14:19:00+00:00
cookie2,2023-01-01T14:19:00+00:00
cookie3,2023-01-01T14:19:00+00:00
cookie4,2023-02-01T14:19:00+00:00
cookie5,2023-01-02T14:19:00+00:00
cookie3,2023-03-01T14:19:00+00:00""")       
    def test_file_with_nontarget_dates_in_file(self, mock_file):
        file_path = "fake_file.csv"
        date = "2023-01-01"
        result = cookie_counter.most_used_cookies(file_path, date)
        self.assertEqual(result.count("\n"), 3) #should be three newlines
        
        expected_result_set = {"cookie1","cookie2","cookie3"}
        # check if all members in the expected result are there
        for item in result.split("\n"):
            if bool(item.strip()):
                self.assertTrue(item in expected_result_set)
                expected_result_set.remove(item)
        
        # check that result has covered every expected result (should be empty if we got every one)
        self.assertEqual(len(expected_result_set), 0)

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_empty_file(self, mock_file):
        file_path = "fake_empty_file.csv"
        date = "2023-01-01"
        result = cookie_counter.most_used_cookies(file_path, date)
        expected_result = "\n"
        self.assertEqual(result, expected_result)

    @patch("builtins.open", new_callable=mock_open, read_data="""cookie,timestamp
cookie1,2023-01-01T14:19:00+00:00
cookie2,2023-02-01T14:19:00+00:00
cookie3,2023-01-01T14:19:00+00:00""")
    def test_no_matching_date(self, mock_file):
        file_path = "fake_file.csv"
        date = "2023-12-31"  # A date with no matching entries
        result = cookie_counter.most_used_cookies(file_path, date)
        expected_result = "\n" 
        self.assertEqual(result, expected_result)
        
    @patch("builtins.open", new_callable=mock_open, read_data="""cookie,timestamp
cookie1,9999-01-01T14:19:00+00:00
cookie2,2023-03-01T14:19:00+00:00
cookie3,2023-02-01T14:19:00+00:00
cookie1,0000-02-01T14:19:00+00:00
cookie2,2018-02-01T14:19:00+00:00
cookie3,2023-02-01T14:19:00+00:00""")
    def test_no_date(self, mock_file):
        file_path = "fake_file.csv"
        date = None
        result = cookie_counter.most_used_cookies(file_path, date)
        self.assertEqual(result.count("\n"), 3) #should be three newlines
        expected_result_set = {"cookie1", "cookie2", "cookie3"}
        
        # check if all members in the expected result are in the result
        for item in result.split("\n"):
            if bool(item.strip()):
                self.assertTrue(item in expected_result_set)
                expected_result_set.remove(item)
        
        # check that result has covered every expected result (should be empty if we got every one)
        self.assertEqual(len(expected_result_set), 0)

if __name__ == "__main__":
    unittest.main()
