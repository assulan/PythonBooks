import bisect
import random
from array import array

text = '''Scotland   Edinburgh  Edinburgh University
Germany    Berlin     University of Berlin'''


def named_slice_example():
    print('\nExample of named slicing')
    COUNTRY = slice(0, 10)
    CAPITAL = slice(11, 20)
    UNIVERISTY = slice(21, None)
    for line in text.split('\n'):
        print('{0}, {1}, {2}'.format(line[COUNTRY], line[CAPITAL], line[UNIVERISTY]))


def binary_search_example(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """Return a letter grade"""
    print('\nExample of binary search')
    index = bisect.bisect(breakpoints, score)
    print(grades[index])


def inorder_insert_example():
    print('\nExample of inorder insert')
    my_list = []
    for i in range(5):
        item = random.randrange(7)
        bisect.insort(my_list, item)
        print('{0:2d} -> {1}'.format(item, my_list))


def array_example():
    print('\nExample of array usage')
    a = array('d')
    for i in range(10):
        a.append(random.randrange(20))
    print(a)
    print(a.itemsize)

    # Sorting the array
    a = array(a.typecode, sorted(a))
    print(a)


def memory_view_example():
    print('\nExample of memory view that allows to share memory between data strucutes, and type casting')
    numbers = array('I', [2, 1, 2, 3])  # short signed integer
    print(numbers)
    memv = memoryview(numbers)
    print(len(memv))
    memv_oct = memv.cast('B')  # octal=unsigned char
    print(memv_oct.tolist())   # individual bytes as a list
    memv_oct[1] = 2            # change in a byte is reflected in original array
    print(numbers)


if __name__ == '__main__':
    named_slice_example()

    print('\nExample of variable unpacking')
    a, b, *c = range(10)
    print(a, b, c)

    binary_search_example(90.5)
    inorder_insert_example()
    array_example()
    memory_view_example()

    # Deque - double ended queue
    print('\n\nDeque example')
    from collections import deque
    dq = deque(range(10), maxlen=4)
    print(dq)