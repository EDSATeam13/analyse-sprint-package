import numpy as np
import pandas as pd


def dictionary_of_metrics(items):
    """
        Calculates the mean, median, variance, standard deviation, minimum and maximum of a list of items.
        Args:
            items (array): list or array-like object containing numerical values.
        Returns:
            dict: dictionary containing the mean, median, variance, standard deviation, minimum and maximum of the given list of items.
    """
    vr_list = []
    for x in items:
        vr_list.append((x - round(np.mean(items), 2)) ** 2)
    variance = round(sum(vr_list) / (len(vr_list) - 1), 2)
    standard_deviation = round((variance) ** 0.5, 2)
    return {
        "mean": round(np.mean(items), 2),
        'median': round(np.median(items), 2),
        'var': round(variance, 2),
        'std': round(standard_deviation, 2),
        'min': round(np.min(items), 2),
        'max': round(np.max(items), 2)
    }
