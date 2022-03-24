from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, TypeRelation
from autodsc.utils.visions.types.categorical import Categorical
from autodsc.utils.visions.types.type import VisionsBaseType


class Ordinal(VisionsBaseType):
    """**Ordinal** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import pandas as pd
        >>> import autodsc.utils.visions
        >>> x = pd.Series([1, 2, 3, 1, 1], dtype='category')
        >>> x in visions.Ordinal
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [IdentityRelation(Categorical)]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
