"""
    Theory of Probability and Mathematical Statistics task
"""

import numpy as np
import data.sequence
import tasks.plotting
import tasks.calculation


def main():
    data_row = data.sequence.row
    variation_row = np.array(sorted(data_row))
    interval_numb = 9

    tasks.plotting.run(data_row, variation_row, interval_numb)
    tasks.calculation.run(data_row, variation_row, interval_numb)


if __name__ == '__main__':
    main()
