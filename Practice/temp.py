integers = [3,4,5]
def pythagorean_triple(integers):
    a = 0
    b = 0
    c = 0
    for i in integers:
        if i == max(i):
            a= a + i
        elif i == min(i):
            b = b + i
        else:
            c = i + c
    return a, b, c

print(pythagorean_triple(integers))