from collections.abc import Iterable, Sized
from typing import Protocol

from matchescu.typing import EntityReferenceIdentifier


class BinaryComparisonSpace(
    Iterable[tuple[EntityReferenceIdentifier, EntityReferenceIdentifier]],
    Sized,
    Protocol,
):
    def put(
        self, left: EntityReferenceIdentifier, right: EntityReferenceIdentifier
    ) -> "BinaryComparisonSpace":
        pass
