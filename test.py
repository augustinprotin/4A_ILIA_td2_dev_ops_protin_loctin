import main
import calendrier as C
from datetime import datetime

date1 = datetime(2025, 10, 24)
date2 = datetime(2026, 10, 24)
date3 = datetime(2024, 10, 24)
ev1 = C.create_event(date1, 1, "Event 1")
ev2 = C.create_event(date2, 2, "Event 2")


def test_hello():
    assert main.hello() == "Hello world !"


def test_create_event():
    assert C.create_event(date3, 3, "Event 3") == (date3, 3, "Event 3")


def test_get_events():
    assert C.get_events() == [ev1, ev2, (date3, 3, "Event 3")]


def test_get_sorted_events():
    assert C.get_sorted_events() == [(date3, 3, "Event 3"), ev1, ev2]


def test_get_first_event_name():
    assert C.get_first_event_name() == "Event 1"
