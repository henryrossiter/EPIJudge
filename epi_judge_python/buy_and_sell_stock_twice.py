from test_framework import generic_test


def buy_and_sell_stock_twice(prices):
    # going forwards
    best_gain_forward_by_day = []
    smallest_seen = float('inf')
    best_gain = 0.0
    for item in prices:
        smallest_seen = min(item, smallest_seen)
        best_gain = max(item - smallest_seen, best_gain)
        best_gain_forward_by_day.append(best_gain)


    # going backwards
    biggest_seen = float('-inf')
    for i, price in reversed(list(enumerate(prices[1:], 1))):
        biggest_seen = max(price, biggest_seen)
        best_gain = max(biggest_seen - price + best_gain_forward_by_day[i-1], best_gain)



    return best_gain




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))
