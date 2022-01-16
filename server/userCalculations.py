import pandas as pd
import numpy as np
import json
from dal import db

from ownMath import pearsonCorrelationCoeff

def calculateCorrelation(userId, x_data_type, y_data_type):

    x_data, y_data = db.getUserData(userId)
    pearsonCorrelationCoeff(x_data, y_data)

    return val, pandas_val