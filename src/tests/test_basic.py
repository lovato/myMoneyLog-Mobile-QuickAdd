'''
Created on 18/10/2012

@author: marco.lovato
'''
from nose.tools import assert_equals

class TestModelOne(object):
    """ Test all methods on ModelOne """

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        """ This method run on every test """
        pass

    def test_basic(self):
        assert_equals(1, 1)
