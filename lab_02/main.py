"""
    Theory of Probability and Mathematical Statistics task
"""

import numpy as np
import data.sequence
import tasks.plotting
import tasks.calculation
import tasks.pearson
import tasks.intervals


def main():
    data_row = data.sequence.row
    variation_row = np.array(sorted(data_row))
    interval_numb = 9

    # tasks.plotting.run(variation_row, interval_numb)
    # tasks.calculation.run(variation_row, interval_numb)
    tasks.pearson.run(variation_row, interval_numb)
    tasks.intervals.run(variation_row, interval_numb)


if __name__ == '__main__':
    main()
