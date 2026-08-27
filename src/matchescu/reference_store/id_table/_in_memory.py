from collections.abc import Iterable, Iterator
from functools import partial

from matchescu.typing import EntityReference, EntityReferenceIdentifier

from matchescu.reference_store._exceptions import EntityReferenceNotFound
from matchescu.reference_store.id_table._protocol import IdTable


class InMemoryIdTable(IdTable):
    def __init__(self):
        self._id_table = {}

    def __len__(self) -> int:
        return len(self._id_table)

    def __iter__(self) -> Iterator[EntityReference]:
        return iter(self._id_table.values())

    def ids(self) -> Iterable[EntityReferenceIdentifier]:
        return self._id_table.keys()

    def put(self, ref: EntityReference) -> IdTable:
        if ref is None:
            return self
        self._id_table[ref.id] = ref
        return self

    def get(self, ref_id: EntityReferenceIdentifier) -> EntityReference:
        if ref_id not in self._id_table:
            raise EntityReferenceNotFound(ref_id)
        return self._id_table[ref_id]

    def get_all(
        self, ref_ids: Iterable[EntityReferenceIdentifier]
    ) -> Iterable[EntityReference]:
        return list(map(self.get, ref_ids))

    @staticmethod
    def __has_source(identifier: EntityReferenceIdentifier, source: str) -> bool:
        return identifier.source == source

    def get_by_source(self, source: str) -> Iterable[EntityReference]:
        has_source = partial(self.__has_source, source=source)
        ids_with_source = filter(has_source, self._id_table.keys())
        return filter(
            lambda ref: ref is not None, map(self._id_table.get, ids_with_source)
        )
