from test_framework import generic_test


def is_symmetric(tree):
    def helper(left_tree, right_tree):
        if not left_tree and not right_tree:
            return True
        elif left_tree and right_tree:
            return left_tree.data == right_tree.data and helper(left_tree.right, right_tree.left) and helper(left_tree.left, right_tree.right)
        return False
    return not tree or helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
