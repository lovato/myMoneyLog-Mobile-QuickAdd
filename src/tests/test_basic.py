'''
Created on 18/10/2012

@author: marco.lovato
'''
import unittest
from append_mml import *

class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.foo = Transactor()
        pass

    def tearDown(self):
        """Call after every test case."""
        pass

    def test_add_transaction(self):
        """Test case A. note that all test method names must begin with 'test.'"""
        transaction = 'aaa'
        self.foo.append_transaction(transaction, 'test.txt')
        assert self.foo.get_last_transaction('test.txt') == transaction

if __name__ == "__main__":
    unittest.main() # run all tests