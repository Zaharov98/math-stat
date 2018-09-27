"""
    Theory of Probability and Mathematical Statistics task
"""

import numpy as np
import data.sequence
from plotting.variation import *


def main():
    data_row = data.sequence.row
    variation_row = np.array(sorted(data_row))

    swing = variation_row[-1] - variation_row[0]

    interval_numb = 9
    h = swing / interval_numb

    x_min = variation_row[0]
    intervals = [(x_min + h * step, x_min + h * (step + 1))
                 for step in range(0, interval_numb + 1)]

    interval_freq = []
    for interval in intervals:
        freq = len(list(filter(lambda x: interval[0] <= x <= interval[1], variation_row)))
        interval_freq.append(freq)
    interval_middle = [(interval[0] + interval[1]) / 2 for interval in intervals]
    freq_polygon.graph(interval_middle, interval_freq)

    relative_freq = [freq / len(data_row) for freq in interval_freq]
    freq_destiny = [freq / h for freq in relative_freq]

    bins = [interval[0] for interval in intervals]
    relative_freq_histogram.graph(freq_destiny, bins)

    empirical_distribution.graph(bins, relative_freq)


if __name__ == '__main__':
    main()
