from sorting.generic_sort import GenericSort


class CombSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)

    def sort(self):
        gap = len(self.col)
        shrink = 1.3
        is_sorted = False

        while is_sorted == False:
            gap = gap // shrink
            if gap > 1:
                is_sorted = False
            else:
                gap = 1
                is_sorted = True

        pos = 0
        while pos + gap < len(self.col):
            if self.col[pos] > self.col[pos + gap]:
                self.col[pos], self.col[pos - 1] = self.col[pos - 1], self.col[pos]
            pos += 1
