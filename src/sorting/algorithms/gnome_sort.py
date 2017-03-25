from sorting.generic_sort import GenericSort


class GnomeSort(GenericSort):
    def __init__(self, col, key, reverse):
        super().__init__(col, key, reverse)

    def sort(self):
#         pos = 0
#         while pos < len(self.col):
#             if (pos == 0 or self.col[pos] >= self.col[pos - 1]):
#                 pos = pos + 1
#             else:
#                 self.col[pos], self.col[pos-1] = self.col[pos-1], self.col[pos]
#                 pos = pos - 1
        pos = 0
        while pos < len(self.col):
            if (pos == 0 or not self._in_order(self.col[pos],self.col[pos - 1]) ):
                pos = pos + 1
            else:
                self.col[pos], self.col[pos-1] = self.col[pos-1], self.col[pos]
                pos = pos - 1