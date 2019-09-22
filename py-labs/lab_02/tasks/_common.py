""" Common functions for all the tasks """


def get_interval_frequency(intervals, variation_row):
    interval_freq = []
    for interval in intervals:
        freq = len(list(filter(lambda x: interval[0] <= x <= interval[1], variation_row)))
        interval_freq.append(freq)

    return interval_freq


def get_sample_mean(row, row_weight):
    return (1 / sum(row_weight)) * sum([row[i] * row_weight[i] for i in range(0, len(row))])


def get_sample_variance(row, row_weight, mean):
    return (1 / sum(row_weight)) * sum([row_weight[i] * (row[i] - mean)**2 for i in range(0, len(row))])


def get_corrected_variance(row, row_weight, mean):
    return (sum(row_weight) / (sum(row_weight) - 1)) * get_sample_variance(row, row_weight, mean)
