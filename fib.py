'''library for fibvonacci numbers'''

def get_fib(n:int) -> int:
    '''return n_th Fibonacci number'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return get_fib(n-2) + get_fib(n-1)
         