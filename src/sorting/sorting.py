'''

@author: radu
'''
from sorting.algorithms.algorithm import Algorithm


class Sorting(object):
    @staticmethod
    def sort(col, key=None, reverse=False, algorithm=Algorithm.GNOME_SORT):
        sorting_alg = algorithm.value(col, key, reverse)
        sorting_alg.sort()
