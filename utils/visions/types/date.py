from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.date_time import DateTime
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.type import VisionsBaseType


class Date(VisionsBaseType):
    """**Date** implementation of :class:`visions.types.type.VisionsBaseType`.
    All values are should be datetime.date or missing

    Examples:
        >>> import datetime
        >>> import autodsc.utils.visions
        >>> x = [datetime.date(2017, 3, 5), datetime.date(2019, 12, 4)]
        >>> x in visions.Date
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [
            IdentityRelation(Object),
            InferenceRelation(DateTime),
        ]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
