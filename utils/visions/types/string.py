from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, TypeRelation
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.type import VisionsBaseType


class String(VisionsBaseType):
    """**String** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> x = ['rubin', 'carter', 'champion']
        >>> x in visions.String
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
