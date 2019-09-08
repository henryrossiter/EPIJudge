from test_framework import generic_test


def merge_two_sorted_arrays(A, m, B, n):
    index = m + n - 1
    i = m - 1
    j = n - 1
    while index >= 0:
        if i >=0 and (j < 0 or A[i] >= B[j]):
            A[index] = A[i]
            i -= 1
        elif j >= 0 and (i < 0 or A[i] < B[j]):
            A[index] = B[j]
            j -=1
        index -= 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sorted_arrays_merge.py",
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
