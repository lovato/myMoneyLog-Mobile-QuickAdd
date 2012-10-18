'''
Created on 18/10/2012

@author: marco.lovato
'''
import unittest
from main import Dummy

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.foo = Dummy()

    def tearDown(self):
        """Call after every test case."""
        pass

    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        assert self.foo.dummyfunc(543) == 543, "bar() not calculating values correctly"

    def testB(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        assert self.foo.dummyfunc(543) == 22, "bar() not calculating values correctly"

if __name__ == "__main__":
    unittest.main() # run all tests