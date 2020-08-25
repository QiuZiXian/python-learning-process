from random import seed, randint
import sys


def f(arg_for_seed, nb_of_elements, max_element):
    # '''
    # >>> f(0, 0, 10)
    # Here is L: []
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     []
    # >>> f(0, 1, 10)
    # Here is L: [6]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6]]
    # >>> f(0, 2, 10)
    # Here is L: [6, 6]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6]]
    # >>> f(0, 3, 10)
    # Here is L: [6, 6, 0]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6], [0]]
    # >>> f(0, 4, 10)
    # Here is L: [6, 6, 0, 4]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6], [0, 4]]
    # >>> f(0, 5, 10)
    # Here is L: [6, 6, 0, 4, 8]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6], [0, 4, 8]]
    # >>> f(0, 6, 10)
    # Here is L: [6, 6, 0, 4, 8, 7]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6], [0, 4, 8], [7]]
    # >>> f(0, 7, 10)
    # Here is L: [6, 6, 0, 4, 8, 7, 6]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[6], [0, 4, 8], [7], [6]]
    # >>> f(3, 10, 6)
    # Here is L: [1, 4, 4, 1, 2, 4, 3, 5, 4, 0]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[1, 4], [1, 2, 4], [3, 5], [4], [0]]
    # >>> f(3, 15, 8)
    # Here is L: [3, 8, 2, 5, 7, 1, 0, 7, 4, 8, 3, 3, 7, 8, 8]
    # The decomposition of L into increasing sequences,
    #     with consecutive duplicates removed, is:
    #     [[3, 8], [2, 5, 7], [1], [0, 7], [4, 8], [3, 7, 8]]
    # '''
    if nb_of_elements < 0:
        sys.exit()
    seed(arg_for_seed)
    L = [randint(0, max_element) for _ in range(nb_of_elements)]
    print('Here is L:', L)
    R = []
    # Insert your code here
    if len(L) > 0:
        item = [L[0]]
        for index, num in enumerate(L):
            if index == len(L) - 1:
                R.append(item)
                break
            if num == L[index + 1]:
                continue
            if num < L[index + 1]:
                item.append(L[index + 1])
            else:
                R.append(item)
                item = [L[index + 1]]

    print('The decomposition of L into increasing sequences,')
    print('    with consecutive duplicates removed, is:\n   ', R)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    f(0, 0, 10)
    f(0, 1, 10)
    f(0, 2, 10)
    f(0, 3, 10)
    f(0, 4, 10)
    f(0, 5, 10)
    f(0, 6, 10)
    f(0, 7, 10)
    f(3, 10, 6)
    f(3, 15, 8)