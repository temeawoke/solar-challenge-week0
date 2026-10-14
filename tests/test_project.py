import numpy as np
import pandas as pd


def test_python_data_libraries_work():
    values = np.array([1, 2, 3])

    assert values.sum() == 6
    assert pd.Series(values).mean() == 2