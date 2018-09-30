""" Task related to the simple calculations """

import math
import tableprint as tp
from . import _common


def _display_result(sample_mean, sample_variance, standard_deviation):
    print('\n')
    print(tp.header(['sample mean', 'sample variance', 'standard deviation', ]))
    print(tp.row([sample_mean, sample_variance, standard_deviation, ]))


def run(variation_row, interval_numb):
    """ Run task related to simple calculations """
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
    _display_result(sample_mean, sample_variance, standard_deviation)

