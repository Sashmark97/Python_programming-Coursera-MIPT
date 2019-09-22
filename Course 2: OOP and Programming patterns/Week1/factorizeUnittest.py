import unittest

'''
def factorize(c):
    pass
'''


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        cases = ("string", 1.5)
        for c in cases:
            with self.subTest(x=c):
                self.assertRaises(TypeError, factorize, c)

    def test_negative(self):
        cases = (-1, -10, -100)
        for c in cases:
            with self.subTest(x=c):
                self.assertRaises(ValueError, factorize, c)

    def test_zero_and_one_cases(self):
        cases = (0, 1)
        for c in cases:
            with self.subTest(x=c):
                self.assertEqual(factorize(c), (c,))

    def test_simple_numbers(self):
        cases = (3, 13, 29)
        for c in cases:
            with self.subTest(x=c):
                self.assertEqual(factorize(c), (c,))

    def test_two_simple_multipliers(self):
        cases = {6: (2, 3), 26: (2, 13), 121: (11, 11)}
        for c in cases:
            with self.subTest(x=c):
                self.assertTupleEqual(factorize(c), cases[c])

    def test_many_multipliers(self):
        self.cases = {1001: (7, 11, 13), 9699690: (2, 3, 5, 7, 11, 13, 17, 19)}
        for c in self.cases:
            with self.subTest(x=c):
                self.assertTupleEqual(factorize(c), self.cases[c])
'''
if __name__ == "__main__":
    unittest.main()
'''
