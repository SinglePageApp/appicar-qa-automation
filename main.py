import unittest
import json


if __name__ == "__main__":
    # Get the tests to run from the config file.
    config = json.loads(open('config.json').read())
    browsers = config['RUN']['browsers']
    tests = config['RUN']['tests']
    # Prepare the test suite.
    suite = unittest.TestSuite()
    module = __import__('workflows.frontend', fromlist=tests)
    # Add the tests to the test suite.
    for browser in browsers:
        for test in tests:
            suite.addTest(eval('module.' + test)(browser_name=browser))
    # Run tests from the defined test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)
