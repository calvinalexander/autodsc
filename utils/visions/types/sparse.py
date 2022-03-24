from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, TypeRelation
from autodsc.utils.visions.types.generic import Generic
from autodsc.utils.visions.types.type import VisionsBaseType


class Sparse(VisionsBaseType):
    """**Sparse** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> import pandas as pd
        >>> import autodsc.utils.visions
        >>> x = pd.Sparse(pd.Series([np.complex(0, 0), np.complex(1, 2), np.complex(3, -1)]))
        >>> x in visions.Sparse
        True
    """

    @staticmethod
    def get_relations() -> Sequence[TypeRelation]:
        relations = [IdentityRelation(Generic)]
        return relations

    @staticmethod
    @multimethod
    def contains_op(item: Any, state: dict) -> bool:
        pass
