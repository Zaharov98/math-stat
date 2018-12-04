
import math
import numpy as np
import data
from plotting.variation import *


def main():
    values = data.values

    r = max(values) - min(values)
    step = r / len(values)

    min_val = min(values)
    intervals = [(min_val + step * i, min_val + step * (i + 1)) for i in range(1, len(values))]
    weights = get_weight(intervals, values)

    sample_mean = sum(values) / len(values)
    sample_variance = 1 / sum(weights) * sum([(x - sample_mean)**2 for x in weights])
    standard_deviation = math.sqrt(sample_variance)
    display_result(sample_mean, sample_variance, standard_deviation)

    interval_start = [interval[0] for interval in intervals]
    relative_freq_histogram.graph(weights, interval_start, width=0.5)

    interval_middles = [(interval[0] + (interval[1] - interval[0]) / 2) for interval in intervals]
    freq_polygon.graph(interval_middles, [w / sum(weights) for w in weights])

    relative_interval_freq = [weight / sum(weights) for weight in weights]
    interval_ends = [interval[1] for interval in intervals]
    empirical_distribution.graph(interval_ends, relative_interval_freq)


def get_weight(intervals, values):
    weights = []
    for interval in intervals[:-1]:
        weight = len(list(filter(lambda x: interval[0] <= x < interval[1], values)))
        weights.append(weight)

    # last interval include both sides
    last_weight = len(list(filter(lambda x: intervals[-1][0] <= x < intervals[-1][1], values)))
    weights.append(last_weight)

    return weights


def display_result(sample_mean, sample_variance, standard_deviation):
    print('\nLab 4 result\n')
    print('Sample mean: {0}'.format(sample_mean))
    print('Sample variance: {0}'.format(sample_variance))
    print('Standard deviation: {0}'.format(standard_deviation))


if __name__ == '__main__':
    main()
