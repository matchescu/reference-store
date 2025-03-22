import pytest

from matchescu.typing import EntityReferenceIdentifier


class EntityReferenceStub(dict):
    id: EntityReferenceIdentifier

    def __init__(self, identifier: EntityReferenceIdentifier, **kwargs):
        super().__init__(**kwargs)
        self.id = identifier


@pytest.fixture
def source():
    return "test"


@pytest.fixture
def label():
    return 1


@pytest.fixture
def ref_id(label, source):
    def _(lbl=None, src=None):
        return EntityReferenceIdentifier(lbl or label, src or source)

    return _


@pytest.fixture
def ref(ref_id, label, source):
    def _(lbl=None, src=None):
        lbl = lbl or label
        src = src or source
        return EntityReferenceStub(ref_id(lbl, src), id=lbl)

    return _


@pytest.fixture
def entity_reference(ref):
    return ref()
