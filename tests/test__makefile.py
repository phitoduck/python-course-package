import pytest


@pytest.fixture
def project():
    print("setup")
    yield
    print("teardown")


def test__linting_passes():
    ...


def test__tests_pass():
    ...


def test__install_succeeds():
    ...
