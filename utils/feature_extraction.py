import pandas as pd
import numpy as np
import seaborn as sns
import sklearn

from autodsc.utils.sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder
# +utils categoryencoders
from autodsc.utils.category_encoders import BinaryEncoder, TargetEncoder 
from autodsc.utils.sklearn.feature_extraction import FeatureHasher

class Encoder:

  def __call__(self, df, label, encoder, n=None, target=None):
    if encoder == "label":
      encoder_fn = LabelEncoder()
      df[label]=encoder_fn.fit_transform(df[label])

    elif encoder == "onehot":
      encoder_fn = OneHotEncoder()
      encoder_fn = encoder_fn.fit_transform(df[[label]]).toarray()
      encoded_columns = pd.DataFrame(encoder_fn)
      df = pd.concat([df, encoded_columns], axis=1)
      df = df.drop([label], axis=1)
      
    elif encoder == "frequency":
      encoder_fn = df.groupby(label).size()/len(df)
      df.loc[:, "{}_freq_encoded".format(label)] = df[label].map(encoder_fn)  
      df = df.drop([label], axis=1)

    elif encoder == "ordinal":
      encoder_fn = OrdinalEncoder()
      encoder_fn.fit([df[label]])
      df[label] = encoder_fn.fit_transform(df[[label]])

    elif encoder == "binary":
      encoder_fn = BinaryEncoder(cols=[label])
      encoded_columns = encoder_fn.fit_transform(df[label])
      df = pd.concat([df, encoded_columns], axis=1)
      df = df.drop([label], axis=1)

    elif encoder == "hash":
      # n_features contains the number of bits you want in your hash value.
      encoder_fn = FeatureHasher(n_features=n, input_type="string")
      encoded_columns = encoder_fn.fit_transform(df[label])
      encoded_columns = encoded_columns.toarray()
      df = pd.concat([df, pd.DataFrame(encoded_columns)], axis=1)
      df = df.drop([label], axis=1)

    elif encoder == "target":
      df.insert(5,"Target", target, True) 
      encoder_fn = TargetEncoder()
      encoded_columns = encoder_fn.fit_transform(df[label], y = df.Target)
      df = pd.concat([df, encoded_columns], axis=1)
  
    return df