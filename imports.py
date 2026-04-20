#Imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import train_test_split

from sklearn.metrics import f1_score


# Method to collect data from parent spreadsheet (Choose 'Raw Data' tab for original data or 'Data' for processed data)
def getData(tab_name):

  sheet = spreadsheet.worksheet(tab_name)

  values = sheet.get_all_values();

  headers = values[0];
  records = values[1:];
  data = pd.DataFrame.from_records(records, columns=headers);

  #de-stringify
  for col in data.columns:
      data[col] = pd.to_numeric(data[col]);

  return data