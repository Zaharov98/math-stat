""" Task related to the plots """

import numpy as np
from . import _common
from plotting.variation import *


def run(data_row, variation_row, interval_numb):
    """ Run tasks related to the plots """
    swing = variation_row[-1] - variation_row[0]
    h = swing / interval_numb

    x_min = variation_row[0]
    intervals = [(x_min + h * step, x_min + h * (step + 1))
                 for step in range(0, interval_numb + 1)]

    interval_freq = _common.get_interval_frequency(intervals, variation_row)
    interval_middle = [(interval[0] + interval[1]) / 2 for interval in intervals]
    freq_polygon.graph(interval_middle, interval_freq)

    relative_freq = [freq / len(data_row) for freq in interval_freq]
    freq_destiny = [freq / h for freq in relative_freq]

    bins = [interval[0] for interval in intervals]
    relative_freq_histogram.graph(freq_destiny, bins)

    empirical_distribution.graph(bins, relative_freq)
