""" Task related to the simple calculations """

from . import _common


def run(data_row, variation_row, interval_numb):
    """ Run task related to simple calculations """
    swing = variation_row[-1] - variation_row[0]
    h = swing / interval_numb

    x_min = variation_row[0]
    intervals = [(x_min + h * step, x_min + h * (step + 1))
                 for step in range(0, interval_numb + 1)]

    interval_freq = _common.get_interval_frequency(intervals, variation_row)
    interval_middle = [(interval[0] + interval[1]) / 2 for interval in intervals]

    print('hello from calculations')
