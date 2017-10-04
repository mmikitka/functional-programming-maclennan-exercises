import unittest
import sys

def all_tests_suite():
    return unittest.TestLoader().loadTestsFromNames([
        'funcprog.tests.core',
        'funcprog.tests.sequence',
    ])

def main():
    runner = unittest.TextTestRunner()
    suite = all_tests_suite()
    raise SystemExit(not runner.run(suite).wasSuccessful())

if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()
