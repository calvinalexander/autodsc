from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.generic import Generic
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


class Boolean(VisionsBaseType):
    """**Boolean** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import autodsc.utils.visions
        >>> x = [True, False, False, True]
        >>> x in visions.Boolean
        True

        >>> x = [True, False, None]
        >>> x in visions.Boolean
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [
            IdentityRelation(Generic),
            InferenceRelation(String),
            InferenceRelation(Object),
        ]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
