from test_framework import generic_test
import collections

def flip_color(x, y, image):
    color = image[x][y]
    q = collections.deque([(x, y)])
    image[x][y] = not image[x][y]
    while q:
        x, y = q.popleft()
        if 0 <= x + 1 < len(image) and 0 <= y < len(image[x + 1]) and image[x + 1][y] == color:
            image[x + 1][y] = not image[x + 1][y]
            q.append((x + 1, y))
        if 0 <= x - 1 < len(image) and 0 <= y < len(image[x - 1]) and image[x - 1][y] == color:
            image[x - 1][y] = not image[x - 1][y]
            q.append((x - 1, y))
        if 0 <= x < len(image) and 0 <= y + 1 < len(image[x]) and image[x][y + 1] == color:
            image[x][y + 1] = not image[x][y + 1]
            q.append((x, y + 1))
        if 0 <= x < len(image) and 0 <= y - 1 < len(image[x]) and image[x][y - 1] == color:
            image[x][y - 1] = not image[x][y - 1]
            q.append((x, y - 1))
    return


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
