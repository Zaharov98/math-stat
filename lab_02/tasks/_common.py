""" Common functions for all the tasks """


def get_interval_frequency(intervals, variation_row):
    interval_freq = []
    for interval in intervals:
        freq = len(list(filter(lambda x: interval[0] <= x <= interval[1], variation_row)))
        interval_freq.append(freq)

    return interval_freq
