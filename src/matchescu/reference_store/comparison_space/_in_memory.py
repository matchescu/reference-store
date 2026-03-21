from collections.abc import Iterator

from matchescu.typing import EntityReferenceIdentifier
from matchescu.reference_store.comparison_space._protocol import BinaryComparisonSpace


class InMemoryComparisonSpace(BinaryComparisonSpace):
    def __init__(self):
        self.__data = {}

    def put(
        self, left_id: EntityReferenceIdentifier, right_id: EntityReferenceIdentifier
    ) -> BinaryComparisonSpace:
        cmp = (left_id, right_id)
        self.__data[cmp] = self.__data.get(cmp, 0) + 1
        return self

    def __len__(self) -> int:
        return len(self.__data)

    def __iter__(
        self,
    ) -> Iterator[tuple[EntityReferenceIdentifier, EntityReferenceIdentifier]]:
        return iter(self.__data.keys())
