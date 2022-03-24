from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


class Path(VisionsBaseType):
    """**Path** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import pathlib
        >>> import autodsc.utils.visions
        >>> x = [pathlib.Path('/home/user/file.txt'), pathlib.Path('/home/user/test2.txt')]
        >>> x in visions.Path
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
