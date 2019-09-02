from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays):
    
    min_heap = [] #stores the current candidates for the next lowest item
    iterators = [iter(x) for x in sorted_arrays]
    for i, it in enumerate(iterators):
        next_item = next(it, None)
        heapq.heappush(min_heap, (next_item, i))

    result = []
    while len(min_heap) > 0:
        smallest_entry, smallest_array_index = heapq.heappop(min_heap)
        result.append(smallest_entry)
        next_item = next(iterators[smallest_array_index], None)
        if next_item is not None:
            heapq.heappush(min_heap, (next_item, smallest_array_index))

    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
