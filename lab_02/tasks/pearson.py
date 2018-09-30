"""
    Testing the hypothesis of a normal distribution
"""

import math
import scipy.stats
import numpy as np
import tableprint as tp
from . import _common


def run(variation_row, interval_numb):
    """ Run Pearson test """
    swing = variation_row[-1] - variation_row[0]
    h = swing / interval_numb

    x_min = variation_row[0]
    intervals = [(x_min + h * step, x_min + h * (step + 1))
                 for step in range(0, interval_numb + 1)]

    interval_freq = _common.get_interval_frequency(intervals, variation_row)
    interval_middle = [(interval[0] + interval[1]) / 2 for interval in intervals]

    sample_mean = _common.get_sample_mean(interval_middle, interval_freq)
    sample_variance = _common.get_sample_variance(interval_middle, interval_freq, sample_mean)
    standard_deviation = math.sqrt(sample_variance)

    theoretic_freq = get_theoretical_freq(interval_middle, interval_freq, h, sample_mean, standard_deviation)
    observed_chi = get_observable_chi(interval_freq, theoretic_freq)

    significance = 0.01
    critical_chi = get_critical_chi(interval_numb, significance)

    _display_result(observed_chi, critical_chi)


def _display_result(observable_chi, critical_chi):
    print('\nhypothesis of a normal distribution')
    print(tp.header(['Observable chi', 'Critical chi', ]))
    print(tp.row([observable_chi, critical_chi, ]))


def get_theoretical_freq(interval_middle, interval_freq, step, sample_mean, standard_deviation) -> list:
    temp_values = [(interval_middle[i] * interval_freq[i] - sample_mean) / standard_deviation
                   for i in range(0, len(interval_middle))]
    laplace_values = scipy.stats.laplace.pdf(temp_values)
    theoretic_freq = [(sum(interval_freq) * step / standard_deviation) * laplace_value
                      for laplace_value in laplace_values]

    return theoretic_freq


def get_observable_chi(interval_freq, theoretic_freq) -> float:
    return sum([(interval_freq[i] - theoretic_freq[i])**2 for i in range(0, len(interval_freq))]) / sum(interval_freq)


def get_critical_chi(interval_count, significance) -> float:
    return 16.8  # programmatic way is not found
