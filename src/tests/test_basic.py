'''
Created on 18/10/2012

@author: marco.lovato
'''
from nose.tools import assert_equals #@UnresolvedImport

class TestModel(object):
    """ Test all methods on ModelOne """

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        """ This method run on every test """
        pass

    def test_basic(self):
        assert_equals(1, 1)
