import pathlib
from typing import Sequence

from autodsc.utils.visions.types.file import File


@File.contains_op.register
def file_contains(sequence: Sequence, state: dict) -> bool:
    return all(isinstance(p, pathlib.Path) and p.exists() for p in sequence)
