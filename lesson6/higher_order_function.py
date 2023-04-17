
def first_function():
    """print first_function"""
    return "first_function"

def second_function():
    """print second_function"""
    return "second_function"

def third_function():
    """print third_function"""
    return "third_function"

print(*map(lambda x: f'{x + 1} ' + first_function(), range(3)),sep = '\n')
print()
print(*map(lambda x: f'{x + 1} ' + second_function(), range(5)),sep = '\n')
print()
print(*map(lambda x: f'{x + 1} ' + third_function(), range(10)),sep = '\n')

