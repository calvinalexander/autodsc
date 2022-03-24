from typing import Sequence

from autodsc.utils.visions.types.categorical import Categorical


@Categorical.contains_op.register
def categorical_contains(sequence: Sequence, state: dict) -> bool:
    return False
