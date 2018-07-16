import unittest
import json


if __name__ == "__main__":
    # Get the tests to run from the config file.
    config = json.loads(open('config.json').read())
    browsers = config['RUN']['browsers']
    tests = config['RUN']['tests']
    # Run tests from the defined test suite.
    suite = unittest.TestSuite()
    module = __import__('workflows.frontend', fromlist=tests)

    for browser in browsers:
        for test in tests:
            suite.addTest(eval('module.' + test)(browser_name=browser))

    unittest.TextTestRunner(verbosity=2).run(suite)
