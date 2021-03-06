import json
from subprocess import run


CMD = [
    'pytest',
    './workflows/frontend/{}.py',
    '--tb=long',
    '--alluredir',
    './results/reports/',
    '--browser={}'
]

if __name__ == "__main__":
    # Get the tests to run from the config file.
    config = json.loads(open('config.json').read())
    browsers = config['RUN']['browsers']
    test_suites = config['RUN']['test-suites']['frontend']
    # Run the test suites on the browsers defined in the configuration file.
    for browser in browsers:
        for test_suite in test_suites:
            CMD[1] = CMD[1].format(test_suite)
            CMD[-1] = CMD[-1].format(browser)
            run(CMD)
