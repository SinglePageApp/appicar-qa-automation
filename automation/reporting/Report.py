from .HTMLTestRunner import HTMLTestRunner
import os
import datetime


class Report(HTMLTestRunner):
    """
    HTML reporting tool.
    """
    FILE_PATH = os.getcwd() + '/results/reports/' + str(datetime.datetime.now()) + '.html'

    def __init__(self):
        super(Report, self).__init__(
            stream=open(self.FILE_PATH, 'w'),
            title='Test Report',
            description='Smoke Tests'
        )
