from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # is it possible to write the letter with the magazine
    letter_dict = collections.Counter(letter_text)
    for item in magazine_text:
        if letter_dict[item]:
            letter_dict[item] -= 1
            if letter_dict[item] == 0:
                del letter_dict[item]
        if not letter_dict:
            return True
    return not letter_dict


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
