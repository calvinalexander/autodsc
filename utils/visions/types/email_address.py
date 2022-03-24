from typing import Any, Sequence

import attr
from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


@attr.s(slots=True)
class FQDA:
    local = attr.ib()
    fqdn = attr.ib()

    @staticmethod
    def from_str(s):
        return _to_email(s)


def _to_email(s) -> FQDA:
    if isinstance(s, FQDA):
        return s
    elif isinstance(s, str):
        return FQDA(*s.split("@", maxsplit=1))
    else:
        raise TypeError("Only strings supported")


class EmailAddress(VisionsBaseType):
    """**EmailAddress** implementation of :class:`visions.types.type.VisionsBaseType`.

    Notes:
        The email address should be a **fully qualified domain address** (FQDA)
        FQDA = local part + @ + fully qualified domain name (FQDN)
        This type

    Examples:
        >>> import autodsc.utils.visions
        >>> x = [FQDA('example','gmail.com'), FQDA.from_str('example@protonmail.com')]
        >>> x in visions.EmailAddress
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
