from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, TypeRelation
from autodsc.utils.visions.types.path import Path
from autodsc.utils.visions.types.type import VisionsBaseType


class File(VisionsBaseType):
    """**File** implementation of :class:`visions.types.type.VisionsBaseType`.
    (i.e. existing path)

    Examples:
        >>> import pathlib
        >>> x = [pathlib.Path('/home/user/file.txt'), pathlib.Path('/home/user/test2.txt')]
        >>> x in visions.File
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [IdentityRelation(Path)]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
