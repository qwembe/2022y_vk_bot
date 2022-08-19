import unittest
import random

from math import dist
from hw.hw_00.main import my_sum, pip_install_verification, my_distant


class MyTestCase(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(my_sum(5, 5), 10, "Sum is not equal!")
        self.assertEqual(my_sum(500, 100000), 100500, "Sum is not equal!")

    def test_pip_install_verification(self):
        self.assertTrue(pip_install_verification())

    def test_distant(self):
        for _ in range(100):
            pointA = tuple(random.randint(0, 100) for _ in range(2))
            pointB = tuple(random.randint(0, 100) for _ in range(2))
            self.assertAlmostEqual(dist(pointA, pointB), my_distant(pointA, pointB), msg="Incorrect realization",
                                   delta=0.00001)


if __name__ == '__main__':
    unittest.main()
