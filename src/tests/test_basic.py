'''
Created on 18/10/2012

@author: marco.lovato
'''
import unittest
from mml_datafile_helper import *
from main import *


class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.foo = Transactor()
        self.foo.set_mml_folder(get_mml_folder())
        self.foo.set_datafile('data-tests.html')

    def tearDown(self):
        """Call after every test case."""
        pass

    def test_add_transaction(self):
        transaction = Transaction('2012-10-23', '2,01', 'Terra', 'gasolina', 'ticket', 'minus', 'yes').get_formatted()
        old_line_count = self.foo.datafile_size + 1
        result = self.foo.append_transaction(transaction)
        if result == False:
            print "Problem adding transaction"
        new_line_count = self.foo.datafile_size
        test1 = old_line_count == new_line_count
        test2 = self.foo.get_last_transaction()[:-1] == transaction

        assert (test1 and test2)

if __name__ == "__main__":
    # run all tests
    unittest.main()
