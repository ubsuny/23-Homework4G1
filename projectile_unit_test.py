"""
Module: projectile_unit_test

This module contains unit tests for the calculate_horizontal_distance function in the
projectile_motion_with_air_resistance module.
"""

import unittest
from projectile_motion_with_air_resistance import calculate_horizontal_distance

class TestCalculateHorizontalDistance(unittest.TestCase):
    """
    This class contains unit tests for the calculate_horizontal_distance function.
    """

    def test_distance_calculation(self):
        """
        Test the distance calculation using the calculate_horizontal_distance function.

        Test case 1:
        x0 = 1.0
        y0 = 0.0
        v0 = 10.0
        launch_angle_deg = 45.0
        m = 0.1

        The expected_distance is 11.28, which is the corrected expected result for these inputs.

        Calculate the actual result and assert that it matches the expected result.
        """
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

if __name__ == '__main__':
    unittest.main()
