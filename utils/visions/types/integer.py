from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.float import Float
from autodsc.utils.visions.types.generic import Generic
from autodsc.utils.visions.types.type import VisionsBaseType


class Integer(VisionsBaseType):
    """**Integer** implementation of :class:`visions.types.type.VisionsBaseType`.
    Examples:
        >>> import pandas as pd
        >>> x = [-1, 1, 2, 3]
        >>> x in visions.Integer
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [
            IdentityRelation(Generic),
            InferenceRelation(Float),
        ]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
