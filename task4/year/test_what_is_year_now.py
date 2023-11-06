import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    @patch("what_is_year_now.urllib.request.urlopen")
    def test_ymd_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            '{"currentDateTime": "2023-12-01"}'.encode()
        )
        self.assertEqual(what_is_year_now(), 2023)

    @patch("what_is_year_now.urllib.request.urlopen")
    def test_dmy_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            '{"currentDateTime": "01.12.2023"}'.encode()
        )
        self.assertEqual(what_is_year_now(), 2023)

    @patch("what_is_year_now.urllib.request.urlopen")
    def test_invalid_format(self, mock_urlopen):
        mock_urlopen.return_value.__enter__.return_value.read.return_value = (
            '{"currentDateTime": "01/12/2023"}'.encode()
        )
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == "__main__":
    unittest.main()
