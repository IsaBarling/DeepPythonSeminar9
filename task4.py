from functools import wraps

def run_multiple_times(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@run_multiple_times(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")