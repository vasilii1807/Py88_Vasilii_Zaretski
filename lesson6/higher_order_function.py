def first_function():
    """print first_function"""
    return "first_function"


def second_function():
    """print second_function"""
    return "second_function"


def third_function():
    """print third_function"""
    return "third_function"


def high_func(func, n=10):
    print(*map(lambda x: f'{x + 1} ' + first_function(), range(n)), sep='\n')
    print()


high_func(first_function(), 3)
high_func(second_function(), 5)
high_func(third_function(), 10)
high_func(first_function())
