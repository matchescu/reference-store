import pytest


from matchescu.reference_store.comparison_space._in_memory import (
    InMemoryComparisonSpace,
)


@pytest.fixture
def sut():
    return InMemoryComparisonSpace()


def test_init(sut):
    assert sut is not None


def test_put(sut, ref_id):
    left = ref_id(1, "test_1")
    right = ref_id(2, "test_2")

    sut.put(left, right)

    assert len(sut) == 1


def test_iter(sut, ref_id):
    left_id = ref_id(1, "test_1")
    right_id = ref_id(2, "test_2")
    sut.put(left_id, right_id)

    actual = list(sut)

    assert actual == [(left_id, right_id)]
