import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    def helper(k, curr_capacity):
        if k < 0:
            return 0
        if table[k][curr_capacity] == -1:
            without_curr_item = helper(k - 1, curr_capacity)
            with_curr_item = 0 if curr_capacity < items[k].weight else items[k].value + helper(k - 1, curr_capacity - items[k].weight)
            table[k][curr_capacity] = max(without_curr_item, with_curr_item)
        return table[k][curr_capacity]

    table = [[-1] * (capacity + 1) for _ in items]
    return helper(len(items) - 1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
