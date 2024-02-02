import queue
from collections import namedtuple, defaultdict, Counter, OrderedDict, deque
from queue import Queue, PriorityQueue
import time
from timeout_decorator import timeout


def run_namedtuple():
    # Example for creating class which inheritance from tuple.
    Point_2d = namedtuple("Point_2D", ["x", "y"])
    new_point = Point_2d(5, 10)
    print(new_point)
    x, y = new_point
    print(f"x is {x} and y is {y}")
    print(f"x is {new_point[0]} and y is {new_point[1]}")
    for item in new_point:
        print(f"item: {item}")

    new_circle = namedtuple("new_circle", ["center_x", "center_y", "_radius"], rename=True)
    # field name cannot start with underscore
    print(new_circle._fields)


def run_default_dict():
    # solve error if trying to get key which not exist.
    new_dict = defaultdict(int)
    print(new_dict[4])


def run_counter():
    new_counter = Counter("abcd")
    print(new_counter)
    new_counter.update("abcd")
    print(new_counter.most_common(2))
    del new_counter["a"]
    print(new_counter)


def run_order_dict():
    # maintaining insertion ordr to the dictionary
    new_dict = OrderedDict({
        "apple": 3
    })
    new_dict["banana"] = 2
    print(new_dict)
    new_dict["fruit"] = 1
    print(new_dict)


def run_queue():
    # use FIFO.
    waiting_list = Queue()
    waiting_list.put("naor")
    waiting_list.put("osher")
    while waiting_list.queue:
        print(waiting_list.get())
    priority_queue = PriorityQueue()
    priority_queue.put((2, "naor"))
    priority_queue.put((1, "osher"))
    while priority_queue.queue:
        print(priority_queue.get())


def run_dequeue():
    # use LIFO.
    waiting_list = deque()
    waiting_list.append("naor")
    waiting_list.append("osher")
    print(waiting_list)
    while waiting_list:
        print(waiting_list.popleft())


def run_zip():
    # get iterators
    letters = ["a", "b", "c"]
    symbols = ["!", "@", "#"]
    numbers = [1, 2, 3]
    new_list = zip(letters, symbols, numbers)  # create tuple
    for item in new_list:
        print(item)

    unzipping = zip(letters, symbols, numbers)
    x, y, z = zip(*unzipping)
    print(x, y, z)


def run_eval_func():
    # globals and local parameters.
    x = eval('10**2')
    print(x)


def run_memory_view():
    # return memory view of object
    x = b'Python Programming'
    new = memoryview(x)
    print(type(new))
    print(new)
    print(new.obj)


def addition(n):
    return n + 5


def run_mapping():
    """
    mapping objects
    if you want to make same operation on each object.
    return an iterator - that mean it evaluate only when need it. implemented in c so it faster.
    ** very good!
    :return:
    """
    new_list = [10, 20, 30]
    my_list = map(addition, new_list)
    print(my_list)
    print(list(my_list))

    # lambada functions
    # Sorting a list of tuples based on the second element
    pairs = [(1, 5), (2, 3), (0, 8)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    print(sorted_pairs)


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def sum_all(*args):
    result = 0
    for num in args:
        result += num
    return result


def run_args_and_kwargs():
    """
    *args: varied number of arguments(many args) - if not sure how many args.
    **kwargs dictionary - arbitrary number of arguments.
    :return:
    """
    print(sum_all(1, 2, 3, 4, 5))
    print_info(name="John", age=25, city="New York")


def run_iterators():
    """
    - implement iter() & next()
    - Collection
    :return:
    """
    numbers = [10, 20, 30, 40, 50, 60]
    new_iterator = iter(numbers)
    print(next(new_iterator))
    print(next(new_iterator))


def new_generator():
    my_list = list(range(1, 101))

    index = 0
    while index < len(my_list):
        print(f"This is stage {index // 10}")
        yield my_list[index:index + 10]
        index += 10


def run_generators():
    """
    declare a function that behaves like an iterator.
    using yield keyword.
    to return a value and pauses the execution while maintaining the internal state.
    return iterator of values.
    # more memory-efficient - useful when working with sequences or data that don't need to be loaded entirely into memory.

    :return:
    """
    gen = new_generator()
    for chunk in gen:
        print(chunk)


# decorator to calculate duration
def calculate_time(func):
    def wrapper(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return wrapper


@calculate_time
def run_decorators(x, y, name):
    time.sleep(2)
    print(x * y)
    print(f"My name is: {name}")
    print("Function executed.")


def run_list_comprehension():
    """
    creating list based on iterable object
    :return:
    """
    numbers = [10, 11, 12, 13, 14, 15]
    new_list = [item for item in numbers if item % 2 == 0]
    print(new_list)
    new_matrix = [[y for y in range(6)] for x in range(2)]
    print(new_matrix)


def run_dict_comprehension():
    """
    creating dict based on iterable object
    :return:
    """
    numbers = [("one", 1), ("two", 2), ("three", 3)]
    new_dict = {key: value for key, value in numbers}
    print(new_dict)

    grades = [10, 20, 30]
    students = ["Avi", "Bibi", "Yossi"]
    final_grades = {x: y for (x, y) in zip(students, grades)}
    print(final_grades)

    new_numbers = [1, 5, 10, 15, 20, 25]
    my_dict = {x: x ** 2 for x in new_numbers if x ** 2 % 4 == 0}
    print(my_dict)


def run_set_comprehension():
    """
    creating set based on iterable object
    :return:
    """
    numbers = [1, 2, 1, 2, 1, 2, 1, 3, 4, 5, 6]
    new_set = {num for num in numbers if num % 2 == 0}
    print(new_set)


def run_tuple_comprehension():
    numbers = [1, 2, 3, 4, 5]
    new_tuple = tuple(var for var in numbers)
    print(new_tuple)


def create_logger():
    import logging
    logging.basicConfig(filename="main.log",
                        format="%(asctime)s - %(levelname)s - %(message)s",
                        level=logging.DEBUG)  # Set the logging level to DEBUG for demonstration purposes

    logger = logging.getLogger()
    logger.debug("Logger initialized: Debug information.")
    logger.info("Logger initialized: Basic information.")
    logger.warning("Logger initialized: Warning! Potential issues.")
    logger.error("Logger initialized: Error occurred. Check the logs.")
    logger.critical("Logger initialized: Critical error! Immediate attention required.")


def main():
    # run_namedtuple()
    # run_default_dict()
    # run_counter()
    # run_order_dict()
    # run_queue()
    # run_dequeue()
    # run_zip()
    # run_eval_func()
    # run_memory_view()
    # run_mapping()
    # run_args_and_kwargs()
    # run_iterators()
    # run_generators()
    # run_decorators(3, 5, name="Naor")
    # run_list_comprehension()
    # run_dict_comprehension()
    # run_set_comprehension()
    # run_tuple_comprehension()
    create_logger()


if __name__ == '__main__':
    main()
