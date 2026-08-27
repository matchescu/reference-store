from collections.abc import Iterable, Sized
from typing import Protocol

from matchescu.typing import EntityReference, EntityReferenceIdentifier


class IdTable(Iterable[EntityReference], Sized, Protocol):
    def ids(self) -> Iterable[EntityReferenceIdentifier]:
        pass

    def get(self, ref_id: EntityReferenceIdentifier) -> EntityReference:
        pass

    def get_all(
        self, ref_ids: Iterable[EntityReferenceIdentifier]
    ) -> Iterable[EntityReference]:
        pass

    def get_by_source(self, source: str) -> Iterable[EntityReference]:
        pass

    def put(self, ref: EntityReference) -> "IdTable":
        pass
