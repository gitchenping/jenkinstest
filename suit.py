import unittest
#my suit
class TestLogin(unittest.TestCase):

    def test_a(self):
        a=1
        b=1
        self.assertEqual(a,b)

    def test_b(self):
        a=1
        b=0
        self.assertEqual(a, b)


def suite():
    suitTest=unittest.TestSuite()

    suitTest.addTest(TestLogin("test_a"))
    suitTest.addTest(TestLogin("test_b"))

    return suitTest

