from test_framework import generic_test
import collections


def can_form_palindrome(s):
    freqs = collections.Counter(s)
    return sum([x % 2 for x in freqs.values()]) <= 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
