from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.complex import Complex
from autodsc.utils.visions.types.generic import Generic
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


class Float(VisionsBaseType):
    """**Float** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import autodsc.utils.visions
        >>> x = [1.0, 2.5, 5.0]
        >>> x in visions.Float
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [
            IdentityRelation(Generic),
            InferenceRelation(String),
            InferenceRelation(Complex),
        ]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
