'''
Created on 18/10/2012

@author: marco.lovato
'''
#pylint: disable-msg=C0103,R0904
import unittest
from mml_datafile_helper import Transactor, Transaction
from main import get_mml_folder


class SimpleTestCase(unittest.TestCase):
    '''
    SimpleTestCase
    '''

    transactor = Transactor()

    def setUp(self):
        '''
        """Call before every test case."""
        '''
        self.transactor.set_mml_folder('.')
        self.transactor.set_datafile('data-tests.html')

    def tearDown(self):
        '''
        """Call after every test case."""
        '''
        pass

    def test_add_transaction(self):
        '''
        test_add_transaction
        '''
        transaction = Transaction('2012-10-23', '2,01', 'Terra', 'gasolina',
                                   'ticket', 'minus', 'yes').get_formatted()
        old_line_count = self.transactor.datafile_size + 1
        result = self.transactor.append_transaction(transaction)
        if result == False:
            print "Problem adding transaction"
        new_line_count = self.transactor.datafile_size
        test1 = old_line_count == new_line_count
        test2 = self.transactor.get_last_transaction()[:-1] == transaction

        assert (test1 and test2)

if __name__ == "__main__":
    # run all tests
    unittest.main()
