""" Laboratory work 1, task 2 """

import math
import pprint
import data.prices
import numpy as np


def display_result(sample_mean, sample_variance, standard_deviation):
    print('\nLab 2 result\n')
    print('Sample mean: {0}'.format(sample_mean))
    print('Sample variance: {0}'.format(sample_variance))
    print('Standard deviation: {0}'.format(standard_deviation))


def get_sample_variance(data_row, sample_mean):
    return (1 / len(data_row)) * sum([(x - sample_mean)**2 for x in data_row])


def main():
    data_row = np.array(data.prices.row)
    pprint.pprint(data_row)

    sample_mean = np.sum(data_row) / len(data_row)
    sample_variance = get_sample_variance(data_row, sample_mean)
    standard_deviation = math.sqrt(sample_variance)
    
    display_result(sample_mean, sample_variance, standard_deviation)


if __name__ == '__main__':
    main()
