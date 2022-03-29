"""

.. module:: category_encoders
  :synopsis:
  :platform:

"""

from autodsc.utils.category_encoders.backward_difference import BackwardDifferenceEncoder
from autodsc.utils.category_encoders.binary import BinaryEncoder
from autodsc.utils.category_encoders.count import CountEncoder
from autodsc.utils.category_encoders.hashing import HashingEncoder
from autodsc.utils.category_encoders.helmert import HelmertEncoder
from autodsc.utils.category_encoders.one_hot import OneHotEncoder
from autodsc.utils.category_encoders.ordinal import OrdinalEncoder
from autodsc.utils.category_encoders.sum_coding import SumEncoder
from autodsc.utils.category_encoders.polynomial import PolynomialEncoder
from autodsc.utils.category_encoders.basen import BaseNEncoder
from autodsc.utils.category_encoders.leave_one_out import LeaveOneOutEncoder
from autodsc.utils.category_encoders.target_encoder import TargetEncoder
from autodsc.utils.category_encoders.woe import WOEEncoder
from autodsc.utils.category_encoders.m_estimate import MEstimateEncoder
from autodsc.utils.category_encoders.james_stein import JamesSteinEncoder
from autodsc.utils.category_encoders.cat_boost import CatBoostEncoder
from autodsc.utils.category_encoders.glmm import GLMMEncoder
from autodsc.utils.category_encoders.quantile_encoder import QuantileEncoder, SummaryEncoder

__version__ = '2.4.0'

__author__ = "willmcginnis", "cmougan"

__all__ = [
    "BackwardDifferenceEncoder",
    "BinaryEncoder",
    "CountEncoder",
    "HashingEncoder",
    "HelmertEncoder",
    "OneHotEncoder",
    "OrdinalEncoder",
    "SumEncoder",
    "PolynomialEncoder",
    "BaseNEncoder",
    "LeaveOneOutEncoder",
    "TargetEncoder",
    "WOEEncoder",
    "MEstimateEncoder",
    "JamesSteinEncoder",
    "CatBoostEncoder",
    "GLMMEncoder",
    "QuantileEncoder",
    "SummaryEncoder",
]
