from pyspark.sql.dataframe import DataFrame
from pyspark.sql.types import NumericType

from autodsc.utils.visions.types.numeric import Numeric


@Numeric.contains_op.register
def numeric_contains(sequence: DataFrame, state: dict) -> bool:
    if len(sequence.schema) != 1:
        return False

    dtype = sequence.schema[0].dataType
    return isinstance(dtype, NumericType)
