from typing import Iterable

import pytest

from matchescu.typing import EntityReferenceIdentifier


class EntityReferenceTuple(tuple):
    id: EntityReferenceIdentifier


def _new_tuple(
    identifier: EntityReferenceIdentifier, value: Iterable
) -> EntityReferenceTuple:
    ref = EntityReferenceTuple(value)
    ref.id = identifier
    return ref


@pytest.fixture
def source():
    return "test"


@pytest.fixture
def label():
    return 1


@pytest.fixture(scope="session")
def new_entity_reference():
    return _new_tuple


@pytest.fixture
def entity_reference(source, label):
    return _new_tuple(EntityReferenceIdentifier(label, source), [label])
