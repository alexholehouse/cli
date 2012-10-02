# Copyright 2012 by Alex Holehouse - see LICENSE for more info
# Contact at alex.holehouse@wustl.edu

""" This is test folder for running unit tests.
"""
import sys
import os
# Add the parent directory (which holds the PTMScoutInterface package)
sys.path.insert(0,os.path.abspath(__file__+"../"))

import FileManagerTests
import InputDBManagerTests
import OutputDBManagerTests
import PTMScoutQueryTests
