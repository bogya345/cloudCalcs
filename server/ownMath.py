import math
import numpy as np

def pearsonCorrelationCoeff(X, Y):
    X = np.array(X)
    Y = np.array(Y)

    numenator = np.sum( (X-X.mean())*(Y-Y.mean()) )
    denominator = np.sqrt( np.sum((X-X.mean()).pow(2)) * np.sum((Y-Y.mean()).pow(2)) )

    r = numenator / denominator

    return r
