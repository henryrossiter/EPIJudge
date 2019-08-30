from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    smallest_seen = float('inf')
    best_gain = 0.0
    for item in prices:
        best_gain = max(item - smallest_seen, best_gain)
        smallest_seen = min(item, smallest_seen)
    return best_gain


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
