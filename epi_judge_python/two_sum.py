from test_framework import generic_test


def has_two_sum(A, t):
    i, j = 0, len(A) - 1
    while i <= j:
        curr_sum = A[i] + A[j]
        if curr_sum < t:
            i += 1
        elif curr_sum > t:
            j -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("two_sum.py", 'two_sum.tsv',
                                       has_two_sum))
