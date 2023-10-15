import unittest
from projectile_motion_with_air_resistance import calculate_horizontal_distance  # Replace 'your_script_name' with the actual name of your script

class TestCalculateHorizontalDistance(unittest.TestCase):

    def test_distance_calculation(self):
        # Test case 1
        x0 = 1.0
        y0 = 0.0
        v0 = 10.0
        launch_angle_deg = 45.0
        m = 0.1

        expected_distance = 11.28  # The corrected expected result for these inputs

        # Calculate the actual result
        actual_distance = calculate_horizontal_distance(x0, y0, v0, launch_angle_deg, m)

        # Assert that the actual result matches the expected result
        self.assertAlmostEqual(actual_distance, expected_distance, places=1)

        # You can add more test cases as needed

if __name__ == '__main__':
    unittest.main()
