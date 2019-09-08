from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    def helper(tree, low_range, high_range):
        if not tree:
            return True
        if not (low_range <= tree.data <= high_range):
            return False
        return helper(tree.left, low_range, tree.data) and helper(tree.right, tree.data, high_range)

    return helper(tree, low_range, high_range)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
