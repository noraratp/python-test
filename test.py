import unittest


class RomanFunction():
    def run(self, number):
        msg = ""
        if number == 1:
            msg += "I"
        return msg


class TestRomanFunction(unittest.TestCase):
    def setUp(self):
        self.roman = RomanFunction()

    def test_number_equal_1_should_return_I(self):
        self.assertEqual(self.roman.run(1), "I")


if __name__ == "__main__":
    unittest.main()
