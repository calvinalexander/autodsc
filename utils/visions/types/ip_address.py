from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


class IPAddress(VisionsBaseType):
    """**IP Address** (v4 and v6) implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> from ipaddress import IPv4Address
        >>> import autodsc.utils.visions
        >>> x = [IPv4Address('127.0.0.1'), IPv4Address('128.0.1.2')]
        >>> x in visions.IPAddress
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [
            IdentityRelation(Object),
            InferenceRelation(String),
        ]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
