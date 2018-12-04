
import math
import numpy as np
import data
from plotting.variation import *


def main():
    interval_index, interval_value = np.array(data.interval_index), np.array(data.interval_value)

    intervals = [(index, index + 1) for index in interval_index]
    interval_middles = [(interval[0] + (interval[1] - interval[0]) / 2) for interval in intervals]
    sample_mean = sum(interval_value) / len(interval_value)
    sample_variance = get_sample_variance(interval_value, sample_mean)
    standard_deviation = math.sqrt(sample_variance)
    display_result(sample_mean, sample_variance, standard_deviation)

    freq_polygon.graph(interval_middles, [w / sum(interval_value) for w in interval_value])

    interval_start = [interval[0] for interval in intervals]
    relative_freq_histogram.graph(interval_value, interval_start, width=0.5)

    relative_interval_freq = [value / sum(interval_value) for value in interval_value]
    interval_ends = [interval[1] for interval in intervals]
    empirical_distribution.graph(interval_ends, relative_interval_freq)


def display_result(sample_mean, sample_variance, standard_deviation):
    print('\nLab 2 result\n')
    print('Sample mean: {0}'.format(sample_mean))
    print('Sample variance: {0}'.format(sample_variance))
    print('Standard deviation: {0}'.format(standard_deviation))


def get_sample_variance(data_row, sample_mean):
    return 1 / len(data_row) * sum([(x - sample_mean)**2 for x in data_row])


if __name__ == '__main__':
    main()
