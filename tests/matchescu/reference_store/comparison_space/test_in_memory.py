import pytest


from matchescu.reference_store.comparison_space._in_memory import (
    InMemoryComparisonSpace,
)
from matchescu.typing import EntityReferenceIdentifier


@pytest.fixture
def sut():
    return InMemoryComparisonSpace()


def test_init(sut):
    assert sut is not None


def test_put(sut, new_entity_reference):
    ref1 = new_entity_reference(EntityReferenceIdentifier(1, "test_1"), [1])
    ref2 = new_entity_reference(EntityReferenceIdentifier(2, "test_2"), [2])

    sut.put(ref1, ref2)

    assert len(sut) == 1


def test_iter(sut, new_entity_reference):
    ref1 = new_entity_reference(EntityReferenceIdentifier(1, "test_1"), [1])
    ref2 = new_entity_reference(EntityReferenceIdentifier(2, "test_2"), [2])
    sut.put(ref1, ref2)

    actual = list(sut)

    assert actual == [(ref1.id, ref2.id)]
