import pytest

from simulator.production import parts_produced

def test_zero_elapsed_time():
    assert parts_produced(0, 10) == 0

def test_normal_case():
    assert parts_produced(100, 10) == 10

def test_negative_elapsed_time_error():
    with pytest.raises(ValueError):
        parts_produced(-10, 10)

def test_zero_cycle_time_error():
    with pytest.raises(ValueError):
        parts_produced(100, 0)