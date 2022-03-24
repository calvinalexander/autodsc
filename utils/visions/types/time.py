from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, TypeRelation
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.type import VisionsBaseType


class Time(VisionsBaseType):
    """**Time** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import datetime
        >>> import autodsc.utils.visions
        >>> x = [datetime.time(10, 8, 4), datetime.time(21, 17, 0)]
        >>> x in visions.Time
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [IdentityRelation(Object)]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
