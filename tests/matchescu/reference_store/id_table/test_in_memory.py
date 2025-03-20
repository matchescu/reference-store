import pytest

from matchescu.reference_store._exceptions import EntityReferenceNotFound
from matchescu.reference_store.id_table._in_memory import InMemoryIdTable
from matchescu.typing import EntityReferenceIdentifier


class EntityReferenceTuple(tuple):
    id: EntityReferenceIdentifier


@pytest.fixture
def entity_reference():
    result = EntityReferenceTuple([1, 2, 3])
    result.id = EntityReferenceIdentifier(1, "test")
    return result


@pytest.fixture
def sut():
    return InMemoryIdTable()


def test_init(sut):
    assert sut is not None


def test_add_one_item(sut, entity_reference):
    sut.put(entity_reference)

    assert len(sut) == 1
    assert sut.get("test", 1) == entity_reference


def test_add_same_item_twice(sut, entity_reference):
    sut.put(entity_reference)
    sut.put(entity_reference)

    assert len(sut) == 1


def test_get_non_existent_item(sut, entity_reference):
    with pytest.raises(EntityReferenceNotFound) as exc_wrapper:
        sut.get("test", 1)

    assert (
        str(exc_wrapper.value)
        == "Entity reference with label '1' from source 'test' not found"
    )


def test_iterate(sut, entity_reference):
    sut.put(entity_reference)

    assert list(sut) == [entity_reference]


def test_filter_by_source(sut):
    ref1 = EntityReferenceTuple([1])
    ref1.id = EntityReferenceIdentifier(1, "test_1")
    sut.put(ref1)
    ref2 = EntityReferenceTuple([2])
    ref2.id = EntityReferenceIdentifier(2, "test_2")
    sut.put(ref2)

    test_1_refs = list(sut.get_by_source("test_1"))
    test_2_refs = list(sut.get_by_source("test_2"))

    assert test_1_refs == [ref1]
    assert test_2_refs == [ref2]
