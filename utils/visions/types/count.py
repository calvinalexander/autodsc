from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, TypeRelation
from autodsc.utils.visions.types.integer import Integer
from autodsc.utils.visions.types.type import VisionsBaseType


class Count(VisionsBaseType):
    """**Count** (positive integer) implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> x = [1, 4, 10, 20]
        >>> x in visions.Count
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [IdentityRelation(Integer)]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
