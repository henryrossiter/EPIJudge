from test_framework import generic_test


def has_three_sum(A, t):
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

    A.sort()
    for item in A:
        if has_two_sum(A, t - item):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
