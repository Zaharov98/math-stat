"""
    Empirical distribution function
"""

import math
import itertools
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Process


def _display_plot(x_nodes, y_nodes):
    """ Display plot using pyplot """
    plt.plot(x_nodes, y_nodes, 'bo', x_nodes, y_nodes, 'k', linewidth=0.4)

    plt.title('Empirical distribution function')
    plt.xticks(x_nodes, x_nodes)
    plt.yticks(y_nodes, ['{0:1.2f}'.format(y) for y in y_nodes])

    plt.ioff()              # disable window interactive mode
    plt.legend(loc='best')  # enable labels in plot
    plt.show()


def _display_plot_async(x_nodes, y_nodes):
    """ Run display plot in another process """
    process = Process(target=_display_plot, args=(x_nodes, y_nodes))
    process.start()


def graph(intervals, relative_freq):
    x_nodes = np.array(intervals)
    y_nodes = list(itertools.accumulate(relative_freq))

    _display_plot_async(x_nodes, y_nodes)
