import pytest


@pytest.fixture(scope="module")
def turn_wifi_on():
    print("turning wifi on")
    yield
    print("turning wifi off")


def test_methodA(turn_wifi_on):
    print("Hi its method A")


def test_methodB(turn_wifi_on):
    print("Hi its method B")