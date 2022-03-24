from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.generic import Generic
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


class Complex(VisionsBaseType):
    """**Complex** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> x = [complex(0, 0), complex(1, 2), complex(3, -1)]
        >>> x in visions.Complex
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [
            IdentityRelation(Generic),
            InferenceRelation(String),
        ]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
