from functools import wraps, lru_cache

def trace_witch_one_args(func):

    func._count = 0

    @wraps(func)
    def wrapper(n):
        print("--" * func._count, f'--> {func.__name__}({n})')
        func._count += 1
        result = func(n)
        func._count -= 1
        print("*--" + '--' * func._count, f' {func.__name__}({n}) = {result!r}')
        return result
    return wrapper

@trace_witch_one_args
@lru_cache
def fib(n: int):
    '''
    fib
    0 1 1 2 3 5 8 13
    :param n:
    :return:
    '''
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(list(map(fib, range(10))))
