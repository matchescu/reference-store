import pytest

from matchescu.reference_store._exceptions import EntityReferenceNotFound
from matchescu.reference_store.id_table._in_memory import InMemoryIdTable
from matchescu.typing import EntityReferenceIdentifier


@pytest.fixture
def sut():
    return InMemoryIdTable()


def test_init(sut):
    assert sut is not None


def test_add_one_item(sut, entity_reference):
    sut.put(entity_reference)

    assert len(sut) == 1
    assert sut.get(EntityReferenceIdentifier(1, "test")) == entity_reference


def test_add_same_item_twice(sut, entity_reference):
    sut.put(entity_reference)
    sut.put(entity_reference)

    assert len(sut) == 1


def test_get_non_existent_item(sut, entity_reference):
    with pytest.raises(EntityReferenceNotFound) as exc_wrapper:
        sut.get(EntityReferenceIdentifier(1, "test"))

    assert (
        str(exc_wrapper.value)
        == "Entity reference with label '1' from source 'test' not found"
    )


def test_iterate(sut, entity_reference):
    sut.put(entity_reference)

    assert list(sut) == [entity_reference]


def test_filter_by_source(sut, new_entity_reference):
    ref1 = new_entity_reference(EntityReferenceIdentifier(1, "test_1"), [1])
    sut.put(ref1)
    ref2 = new_entity_reference(EntityReferenceIdentifier(2, "test_2"), [2])
    sut.put(ref2)

    test_1_refs = list(sut.get_by_source("test_1"))
    test_2_refs = list(sut.get_by_source("test_2"))

    assert test_1_refs == [ref1]
    assert test_2_refs == [ref2]
