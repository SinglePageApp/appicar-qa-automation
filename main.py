from automation.data import CONFIG
from subprocess import run


CMD = [
    'pytest',
    './workflows/frontend/{}.py',
    '-s',
    '--capture=no',
    '--tb=long',
    '--alluredir',
    './results/reports/',
    '--browser={}'
]

if __name__ == "__main__":
    # Get the tests to run from the config file.
    browsers = CONFIG['RUN']['browsers']
    test_suites = CONFIG['RUN']['test-suites']['frontend']
    # Run the test suites on the browsers defined in the configuration file.
    for browser in browsers:
        cmd = CMD.copy()
        cmd[-1] = cmd[-1].format(browser)
        for test_suite in test_suites:
            cmd[1] = cmd[1].format(test_suite)
            run(cmd)
