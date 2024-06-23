import timeit


def timer(func):
    """
    Decorator that measures the execution time of a function.

    Args:
        func (callable): The function to be timed.

    Returns:
        callable: The decorated function.
    """

    def wrapper(*args, **kwargs):
        start = timeit.default_timer()
        result = func(*args, **kwargs)
        end = timeit.default_timer()
        time_taken = end - start
        print(f"Time taken to run function {func.__name__}: {time_taken: .6f} seconds")
        return result

    return wrapper
