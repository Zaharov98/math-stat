""" Task related to trustful intervals of sample mean and standard deviation """

import math
from . import _common


def run(variation_row, interval_numb):
    """ Run intervals task """
    swing = variation_row[-1] - variation_row[0]
    h = swing / interval_numb

    x_min = variation_row[0]
    intervals = [(x_min + h * step, x_min + h * (step + 1))
                 for step in range(0, interval_numb + 1)]

    interval_freq = _common.get_interval_frequency(intervals, variation_row)
    interval_middle = [(interval[0] + interval[1]) / 2 for interval in intervals]

    sample_mean = _common.get_sample_mean(interval_middle, interval_freq)
    corrected_variance = _common.get_corrected_variance(interval_middle, interval_freq, sample_mean)
    corrected_standard_deviation = math.sqrt(corrected_variance)

    accuracy = 0.95
    mean_left, mean_right = get_mean_trust_intervals(sum(interval_freq), sample_mean,
                                                     corrected_standard_deviation, accuracy)
    deviation_left, deviation_right = get_deviation_trust_interval(sum(interval_freq),
                                                                   corrected_standard_deviation, accuracy)
    _display_result((mean_left, mean_right), (deviation_left, deviation_right))


def _display_result(mean_interval, deviation_interval):
    """ display the result """
    print('\n')
    print('({0:.3} , {1:.3})'.format(mean_interval[0], mean_interval[1]))
    print('({0:.3} , {1:.3})'.format(deviation_interval[0], deviation_interval[1]))


def get_mean_trust_intervals(count, sample_mean, corrected_standard_deviation, accuracy):
    """ :returns left and right borders of trustful sample mean interval """
    t = _get_mean_intervals_corrector(count, accuracy)
    left = sample_mean - corrected_standard_deviation / math.sqrt(count) * t
    right = sample_mean + corrected_standard_deviation / math.sqrt(count) * t

    return left, right


def get_deviation_trust_interval(count, corrected_deviation, accuracy):
    """ :returns left and right borders of trustful standard deviation interval """
    q = _get_deviation_intervals_corrector(count, accuracy)
    left = corrected_deviation * (1 - q)
    right = corrected_deviation * (1 + q)

    return left, right


def _get_mean_intervals_corrector(count, accuracy):
    """ :returns multiplier of interval count expression (T of y) """
    if count != 100 and accuracy != 0.95:
        raise NotImplementedError('Multiplier for {0} and {1} not specified'.format(count, accuracy))

    return 1.96


def _get_deviation_intervals_corrector(count, accuracy):
    """ :returns multiplier of interval count expression (Q) """
    if count != 100 and accuracy != 0.95:
        raise NotImplementedError('Multiplier for {0} and {1} not specified'.format(count, accuracy))

    return 0.143
