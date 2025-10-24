import main
import calendrier as C
from datetime import datetime

date = datetime(2025, 10, 24)


def test_hello():
    assert main.hello() == "Hello world !"


def test_create_event():
    assert C.create_event(date, 2, "Event") == (date, 2, "Event")


def test_get_events():
    assert C.get_events() == [(date, 2, "Event")]
