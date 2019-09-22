"""
    Relative frequency histogram
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process


def _display_histogram(values, bins, width):
    """ Display the histogram """
    plt.bar(bins, values, width=width)
    plt.xticks(bins, bins)

    plt.xlabel('intervals')
    plt.ylabel('relative frequency')
    plt.title('Relative frequency histogram')

    plt.ioff()              # disable window interactive mode
    plt.grid(True)          # enable grid view
    plt.show()


def _display_histogram_async(values, bins, width):
    """ Run _display_hostogram in another process """
    process = Process(target=_display_histogram, args=(values, bins, width))
    process.start()


def graph(frequencies, intervals, width=17):
    """ Display relative frequency histogram """
    _display_histogram_async(frequencies, intervals, width)
