import logging

logger = logging.getLogger(__name__)


try:
    import pandas as pd

    import autodsc.utils.visions.backends.pandas
    from autodsc.utils.visions.backends.pandas.test_utils import pandas_version

    if pandas_version[0] < 1:
        from autodsc.utils.visions.dtypes.boolean import BoolDtype
    logger.info(f"Pandas backend loaded {pd.__version__}")

except ImportError:
    logger.info("Pandas backend NOT loaded")


try:
    import numpy as np

    import autodsc.utils.visions.backends.numpy

    logger.info(f"Numpy backend loaded {np.__version__}")
except ImportError:
    logger.info("Numpy backend NOT loaded")


try:
    import pyspark

    import autodsc.utils.visions.backends.spark

    logger.info(f"Pyspark backend loaded {pyspark.__version__}")
except ImportError:
    logger.info("Pyspark backend NOT loaded")


try:
    import autodsc.utils.visions.backends.python

    logger.info("Python backend loaded")
except ImportError:
    logger.info("Python backend NOT loaded")
