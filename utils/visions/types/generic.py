from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import TypeRelation
from autodsc.utils.visions.types.type import VisionsBaseType


class Generic(VisionsBaseType):
    """**Generic** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import numpy as np
        >>> import autodsc.utils.visions
        >>> x = ['a', 1, np.nan]
        >>> x in visions.Generic
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        return []

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        return True
