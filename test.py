import main
import calendar as C
from datetime import datetime


def test_hello():
    assert main.hello() == "Hello world !"


def test_create_event():
    date = datetime(2025, 10, 24)
    assert C.create_event(date, 2, "Event") == (date, 2, "Event")
