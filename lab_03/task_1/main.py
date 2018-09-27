"""
    Theory of Probability and Mathematical Statistics task
"""

import math
import data.sequence
from plotting.variation import *


def display_result(sample_mean, sample_variance, standard_deviation):
    print('\nLab 2 result\n')
    print('Sample mean: {0}'.format(sample_mean))
    print('Sample variance: {0}'.format(sample_variance))
    print('Standard deviation: {0}'.format(standard_deviation))


def get_sample_variance(row, weights, sample_mean, count):
    return (1 / count) * sum([n * (x - sample_mean) ** 2 for x, n in zip(row, weights)])


def main():
    data_row = data.sequence.row
    data_weight = data.sequence.weight
    n = 44

    interval_middles = [(interval[0] + (interval[1] - interval[0]) / 2) for interval in data_row]

    sample_mean = sum([interval_middles[i] * data_weight[i] for i in range(0, len(interval_middles))]) / n
    sample_variance = get_sample_variance(interval_middles, data_weight, sample_mean, n)
    standard_deviation = math.sqrt(sample_variance)
    display_result(sample_mean, sample_variance, standard_deviation)

    freq_polygon.graph(interval_middles, data_weight)
    relative_freq_histogram.graph(data_weight, interval_middles)


if __name__ == '__main__':
    main()
