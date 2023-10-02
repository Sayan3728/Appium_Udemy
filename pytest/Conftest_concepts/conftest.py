import pytest


@pytest.fixture(scope="session")
def turn_wifi_on():
    print("turning wifi on")
    yield
    print("turning wifi off")
@pytest.fixture()
def cleanup():
    print("Not Now")
    yield
    print("Clean up is done")