from typing import Any, Sequence

from multimethod import multimethod

from autodsc.utils.visions.relations import IdentityRelation, InferenceRelation, TypeRelation
from autodsc.utils.visions.types.object import Object
from autodsc.utils.visions.types.string import String
from autodsc.utils.visions.types.type import VisionsBaseType


class URL(VisionsBaseType):
    """**Url** implementation of :class:`visions.types.type.VisionsBaseType`.

    Examples:
        >>> from urllib.parse import urlparse
        >>> urls = ['http://www.cwi.nl:80/%7Eguido/Python.html', 'https://github.com/pandas-profiling/pandas-profiling']
        >>> x = [urlparse(url) for url in urls]
        >>> x in visions.URL
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
