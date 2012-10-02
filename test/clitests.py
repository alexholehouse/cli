import unittest
import os
from PTMScoutInterface import PTMScoutQuery

class TestCliFunctions(unittest.TestCase):
    
    def setUp(self):
        
        directory = os.path.dirname(__file__)
        filename = "/testdata.txt"
        
        self.querymanager = PTMScoutQuery.PTMScoutQuery(directory+filename, "file")


    def test_Example(self):
        self.assertEquals(1,1)
