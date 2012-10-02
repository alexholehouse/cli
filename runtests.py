import tests
import unittest


suite = unittest.TestLoader().loadTestsFromTestCase(tests.clitests.TestCLIFunctions)

unittest.TextTestRunner(verbosity=2).run(suite)

