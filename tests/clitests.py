import unittest
import os
from cli import cli

class TestCLIFunctions(unittest.TestCase):
    
    def setUp(self):
        self.displayString = "This is the test string"
        pass

    def seperator(self):
        ## this is so meta, but use the print_terminal_line to help deliniate tests!
        print("\n")
        cli.print_terminal_line("_")

    def test_print_terminal_line(self):
        print "\nBelow should be a line of '!' which extend for the length of the window. Try rerunning at different sizes\n\n"
        cli.print_terminal_line("!")
        self.seperator()

    def test_print_terminal_line_with_ofset(self):
        print "\nBelow should be a line of '!' which extend for the length of the window. Try rerunning at different sizes\n\n"
        cli.print_terminal_line("!", 0.5)
        self.seperator()

    def test_print_in_middle(self):
        print "\nBelow should be the message [" + self.displayString  + "] in the middle of the terminal window. Try rerunning at different sizes\n\n"
        cli.print_in_middle(self.displayString)
        self.seperator()
    
    def test_print_in_middle_with_border(self):
        print "\nBelow should be the message [" + self.displayString  + "] in the middle of the terminal window with a border.\nTry rerunning at different sizes\n\n"
        cli.print_in_middle(self.displayString, "|")
        self.seperator()

    def test_big_message(self):
        print "\nBelow should be the message [" + self.displayString  + "] displayed as a 'big message' \n\n"
        cli.print_big_message(self.displayString)
        self.seperator()

    def test_warning_and_continue(self):
        print "\n"
        cli.warning_and_continue("Test Warning Message")
        self.seperator()

    def test_clear_screen(self):
        print "Testing screen clear...\n\n"
        cli.clear_screen()     
        print "Screen should have cleared\n\n"
        self.seperator()
        
    # z added so it runs last!
    def test_z_quiting_and_aborting_methods(self):
        self.autoAbortTest()
        self.seperator()
        self.error_and_quit_test()

    def autoAbortTest(self):
        print "Testing autoAbort method"
        try:
            cli.autoAbort()
        except SystemExit, e:
            self.assertEquals(e.code,0)
            
    def error_and_quit_test(self):
        print "Testing error and quit"
        try:
            cli.error_and_quit()
        except SystemExit, e:
            self.assertEquals(e.code,1)

    
        
