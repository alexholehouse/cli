import unittest
import os
from cli import cli

class TestCLIFunctions(unittest.TestCase):
    
    def setUp(self):
        self.displayString = "This is the test string"
        pass
        
    def test_Example(self):
        self.assertEquals(1,1)

    def test_print_terminal_line(self):
        print "\nBelow should be a line of '!' which extend for the length of the window. Try rerunning at different sizes"
        cli.print_terminal_line("!")

    def test_print_terminal_line_with_ofset(self):
        print "\nBelow should be a line of '!' which extend for the length of the window. Try rerunning at different sizes"
        cli.print_terminal_line("!", 0.5)

    def test_print_in_middle(self):
        print "\nBelow should be the message [" + self.displayString  + "] in the middle of the terminal window. Try rerunning at different sizes\n"
        cli.print_in_middle(self.displayString)
        print "\n"
    
    def test_print_in_middle_with_border(self):
        print "\nBelow should be the message [" + self.displayString  + "]  in the middle of the terminal window. Try rerunning at different sizes\n"
        cli.print_in_middle(self.displayString, "|")
        print "\n"

    def test_remaining_functions(self):
        
        cli.warning_and_continue("Test Warning Message")
        cli.clear_screen()      
    
