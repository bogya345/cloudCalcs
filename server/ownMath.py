import math
import numpy as np
import scipy.stats as stats

def pearsonCorrelationCoeff(X, Y):
    X = np.array(X)
    Y = np.array(Y)

    numenator = np.sum( (X-X.mean())*(Y-Y.mean()) )
    denominator = np.sqrt( np.sum((X-X.mean())**2) * np.sum((Y-Y.mean())**2) )

    r = numenator / denominator

    return r

def pearsonCorrelationCoeff_scipy(X, Y):
    X = np.array(X)
    Y = np.array(Y)

    r = stats.pearsonr(X, Y)

    return r