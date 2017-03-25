'''

@author: radu
'''
from enum import Enum, unique

from sorting.algorithms.bubble_sort import BubbleSort
from sorting.algorithms.bubble_sort import BubbleSort2
from sorting.algorithms.comb_sort import CombSort
from sorting.algorithms.gnome_sort import GnomeSort
from sorting.algorithms.insertion_sort import InsertionSort, InsertionSortRec
from sorting.algorithms.merge_sort import MergeSort
from sorting.algorithms.quick_sort import QuickSort


@unique
class Algorithm(Enum):
    BUBBLE_SORT = BubbleSort
    BUBBLE_SORT2 = BubbleSort2
    INSERTION_SORT = InsertionSort
    INSERTION_SORT_REC = InsertionSortRec
    QUICK_SORT = QuickSort
    MERGE_SORT = MergeSort
    GNOME_SORT = GnomeSort
    COMB_SORT = CombSort
