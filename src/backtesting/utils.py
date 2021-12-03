import numpy as np

def diffFromPrices(ps):
    return np.diff(ps, prepend=ps[0])

def returnsFromPrices(ps):
    diff = diffFromPrices(ps)
    rdiff = diff/ps

def priceFromReturns(rs, p0 = 1):
    return p0*np.cumprod(1+rs)

def closeToZero(x, epsilon = 1e-06):
    return x > -epsilon and x < epsilon

# test above
closeToZero(np.sum(priceFromReturns(np.array([.1, -.09]), 100) - np.array([110, 100.1])))

# see https://towardsdatascience.com/calculating-sharpe-ratio-with-python-755dcb346805
def sharpeRatio(ts):
    s = ts.mean()/ts.std()
    return (252**.5)*s