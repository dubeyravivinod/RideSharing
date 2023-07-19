import unittest
import sys
from io import StringIO
from Logic.rider_sharing import add_driver, add_rider, match, bill, start_ride, stop_ride


class RideSharingTest(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def assertOutput(self, expected_output):
        self.assertEqual(self.output.getvalue().strip(), expected_output.strip())

    def test_match_no_drivers(self):
        match('R1')
        self.assertOutput('NO_DRIVERS_AVAILABLE')

    def test_match_one_driver(self):
        add_driver('D1', 1, 1)
        add_rider('R1', 0, 0)
        match('R1')
        self.assertOutput('DRIVERS_MATCHED D1')

    # def test_match_multiple_drivers(self):
    #     add_driver('D1', 1, 1)
    #     add_driver('D2', 4, 5)
    #     add_driver('D3', 2, 2)
    #     add_rider('R1', 0, 0)
    #     match('R1')
    #     self.assertOutput('DRIVERS_MATCHED D1 D3')

    def test_start_ride_invalid_ride(self):
        start_ride('RIDE-11', 11, 'R1')
        self.assertOutput('INVALID_RIDE')

    def test_start_ride_invalid_driver(self):
        add_rider('R15', 0, 0)
        start_ride('RIDE-012', 1, 'R15')
        self.assertOutput('INVALID_RIDE')


if __name__ == '__main__':
    unittest.main()
