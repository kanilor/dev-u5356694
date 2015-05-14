"""The metrics module implements functions assessing prediction error for specific purposes."""

import numpy as np
import sklearn.metrics
def trapz(x, y):
    """Trapezoidal rule for integrating
    the curve defined by x-y pairs.
    Assume x and y are in the range [0,1]
    """
    assert len(x) == len(y), 'x and y need to be of same length'
    x = np.concatenate([x, array([0.0, 1.0])])
    y = np.concatenate([y, array([0.0, 1.0])])
    sort_idx = np.argsort(x)
    sx = x[sort_idx]
    sy = y[sort_idx]
    area = 0.0
    for ix in range(len(x)-1):
        area += 0.5*(sx[ix+1]-sx[ix])*(sy[ix+1]+sy[ix])
    return area

def auc(y_true, y_score):
    return sklearn.metrics.roc_auc_score(y_true, y_score)

test_score = [i/10 for i in range(10)]
test_true = 5*[0] + 5*[1]
print(auc(test_true, test_score))
print(test_score, test_true)
