import pytest
from utils import arrs


@pytest.fixture()
def date():
    return [1, 2, 3]


def test_get(date):
    assert arrs.get(date, 1, "test") == 2
    with pytest.raises(IndexError):
        assert arrs.get([], 0, "test") == "test"
    assert arrs.get(date, -1, 'test') == 'test'


def test_slice(date):
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice(date, 1) == [2, 3]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(date, -4) == date
    assert arrs.my_slice(date, -2) == [2, 3] [2, 3]