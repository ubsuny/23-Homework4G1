# Github actions

We choose HW3G5 projectile motion with air resistance

## library

we use `numpy` `pytest` and`pylint`

## unit testing

```python
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
```
return the result
```
Ran 1 test in 0.005s

OK
```
## linting
We used pylint for linting the unit test python file as well as main algorithm python file

```yml
name: Projectile Motion with Air Resistance

on:
  push:
    branches:
      - main
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.11  # Python version

    - name: Install dependencies
      
      run:
        python -m pip install --upgrade pip
        # pip install -r requirements.txt  
    - name: Install linter
      run:
        pip install pylint
    - name: List directory contents
      run: ls -al
    - name: lint projectile_unit_test.py
      run: pylint projectile_unit_test.py  

    
```


### Output example:
first time linting using `pylint` 

![Alt text](https://user-images.githubusercontent.com/143649458/275564730-f8f09bf0-73e6-444b-9a1e-f8d748c1bf6b.png)
failing, first time code rated 7.14/10


![Alt text](https://user-images.githubusercontent.com/143649458/275567084-af4e83d4-509e-4ef1-abeb-8abf4ee4190b.png)

failing, second time code rated 9.29/10



![Alt text](https://user-images.githubusercontent.com/143649458/275569033-72a9e4f2-d7e7-46ee-8a52-19d57d9d6202.png)

passing, third time code rated 10/10

## pytest

```python
# test_example.py

import pytest

def test_addition():
    assert 1 + 1 == 2

def test_subtraction():
    assert 3 - 2 == 1

```
## requirement

```
numpy
pytest
pylint
```

## License

Apache License Version 2.0, January 2004
http://www.apache.org/licenses/


