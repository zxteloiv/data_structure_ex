class MergeSort:
    @staticmethod
    def _merge(arr, aux, lo, mid, hi):
        for i in range(lo, hi+1):
            aux[i] = arr[i]

        i, j = lo, mid + 1
        for k in range(lo, hi + 1):
            if i > mid:
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1

    @staticmethod
    def _sort(arr, aux, lo, hi):
        if lo >= hi: return
        mid = (hi - lo) / 2 + lo
        MergeSort._sort(arr, aux, lo, mid)
        MergeSort._sort(arr, aux, mid + 1, hi)
        MergeSort._merge(arr, aux, lo, mid, hi)

    @staticmethod
    def Sort(arr, len):
        aux = [0] * len
        MergeSort._sort(arr, aux, 0, len - 1)
