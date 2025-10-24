import main
import calendrier as C
from datetime import datetime

tmp1 = datetime(2025, 10, 24).timestamp()
tmp2 = datetime(2026, 10, 24).timestamp()
tmp3 = datetime(2024, 10, 24).timestamp()
ev1 = C.create_event(tmp1, 1, "Event 1")
ev2 = C.create_event(tmp2, 2, "Event 2")


def test_hello():
    assert main.hello() == "Hello world !"


def test_create_event():
    assert C.create_event(tmp3, 3, "Event 3") == (tmp3, 3, "Event 3")


def test_get_events():
    assert C.get_events() == [ev1, ev2, (tmp3, 3, "Event 3")]


def test_get_sorted_events():
    assert C.get_sorted_events() == [(tmp3, 3, "Event 3"), ev1, ev2]


def test_get_first_event_name():
    assert C.get_first_event_name() == "Event 1"
