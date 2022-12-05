
from datetime import datetime

def fib_rec(n: int):
    if n < 2:
        return n
    return fib_rec(n - 1) + fib_rec(n - 2)

# start_rec = time.time()
# result_rec = fib_rec(34)
# end_rec = time.time()
# print(f'Вычисление заняло числа фибоначи рекурсией {result_rec} заняло:  {end_rec - start_rec:0.3f} секунд') 



def fib_while(n: int):
    i = 0
    fib1 = 1
    fib2 = 1
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib_sum
    


# start_while = datetime.now()
# print(start_while)
# result_while = fib_while(34)
# end_while = datetime.now()
# print(end_while)
# td = (end_while - start_while).total_seconds() * 10 * 3
# print(td)
# print(f'Вычисление заняло числа фибоначи while"om {result_while} заняло:  {td:.03f} секунд') 

def fib_for(n: int):
    fib1 = 1
    fib2 = 1
    for i in range(2, n):
        fib3 = fib1 + fib2
        fib1 = fib2
        fib2 = fib3
    return  fib3 #f'fib1 = {fib1}, fib2={fib2}, fib3={fib3}'


# start_for = time.perf_counter()
# result_for = fib_for(34)
# end_for = time.perf_counter()
# print(f'Вычисление заняло числа фибоначи for"om {result_for} заняло:  {end_for - start_for:0.3f} секунд') 


def fib_for_another(n):
    fib1 = 1
    fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
    return  fib2 #f'fib1 = {fib1}, fib2={fib2}'


# start_for_another = time.perf_counter()   
# result_for_another = fib_for(34)
# end_for_another = time.perf_counter()
# print(f'Вычисление заняло числа фибоначи for_another {result_for_another} заняло:  {end_for_another - start_for_another:0.3f} секунд') 


def fib_gen(n):
    a, b = 1, 1
    yield a
    yield b
    for i in range(2, n):
        a, b = b, a + b
        yield f'fib1 = {a}\nfib2 = {b}'

# start_gen = time.perf_counter()
# gen = [fib_gen(i) for i in range(10) if i % 5702887 == 0]
# end_gen = time.perf_counter()
# print(f'Вычисление заняло числа фибоначи for_another {gen} заняло:  {end_gen - start_gen:0.3f} секунд') 



