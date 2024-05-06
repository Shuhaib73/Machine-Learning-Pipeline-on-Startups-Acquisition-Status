# Importing Essential Libraries:

import pandas as pd
import numpy as np

# Importing modules for data preprocessing and model evaluation

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn import metrics

from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_selection import SelectKBest
from imblearn.over_sampling import SMOTE

import pickle
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.base import TransformerMixin

import warnings

pd.set_option('display.max_columns', 100)   # Set pandas options to display a maximum of 100 columns
warnings.filterwarnings('ignore')           # Ignore warnings to enhance code readability


# Custom transformer class for integrating SMOTE (Synthetic Minority Over-sampling Technique) with scikit-learn pipelines.

class SMOTETransformer(TransformerMixin):
    def __init__(self, random_state=None):
        self.random_state = random_state
        self.smote = SMOTE(random_state=random_state)

    def fit(self, X, y=None):
        # SMOTE should not be fit during the training phase
        return self

    def transform(self, X, y=None):
        if y is None:
            # Return input data unchanged if target labels are not provided (e.g., during transformation)
            return X
        else:
            # Apply SMOTE transformation during training phase
            X_resampled, y_resampled = self.smote.fit_resample(X, y)
            return X_resampled, y_resampled


class PipelineTester:
  def __init__(self, pipeline_path: str, test_data: pd.DataFrame):
    self.pipeline_path = pipeline_path
    self.test_data = test_data

  def predict(self):
    with open(self.pipeline_path, 'rb') as file:
      loaded_pipeline = pickle.load(file)

    # Get the probability scores for each class
    predicted_class = loaded_pipeline.predict(self.test_data)

    return predicted_class
 
