from test_framework import generic_test


def is_well_formed(s):
    lookup_dict = {'(':')', '{':'}', '[':']'}
    stack = []

    for letter in s:
        if letter in lookup_dict:
            stack.append(letter)
        else:
            if not stack:
                return False
            top_element = stack.pop()
            if lookup_dict[top_element] != letter:
                return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
