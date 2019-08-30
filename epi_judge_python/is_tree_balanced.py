from test_framework import generic_test
import collections

def is_balanced_binary_tree(tree):
    BalancedWithHeight = collections.namedtuple('BalancedWithHeight', ('balanced', 'height'))
    def helper(tree):
        if not tree:
            return BalancedWithHeight(True, -1)

        left_result = helper(tree.left)
        if not left_result.balanced:
            return BalancedWithHeight(False, 0)

        right_result = helper(tree.right)
        if not right_result.balanced:
            return BalancedWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1

        return BalancedWithHeight(is_balanced, height)

    return helper(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
