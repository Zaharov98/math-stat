"""
    Theory of Probability and Mathematical Statistics task
"""

import data.intervals
from plotting.variation import *


def main():
    intervals = data.intervals.borders
    weights = data.intervals.weight
    n = sum(weights)

    interval_middles = [(interval[0] + (interval[1] - interval[0]) / 2) for interval in intervals]

    freq_polygon.graph(interval_middles, weights)
    relative_freq_histogram.graph(weights, interval_middles)

    relative_interval_freq = [weight / n for weight in weights]
    interval_ends = [interval[1] for interval in intervals]
    empirical_distribution.graph(interval_ends, relative_interval_freq)


if __name__ == '__main__':
    main()
