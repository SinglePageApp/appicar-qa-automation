import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="Firefox", help="browser: Firefox or Chrome"
    )


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--browser")
