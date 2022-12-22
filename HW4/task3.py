def integers():
    int_num = 1
    while True:
        yield int_num
        int_num += 1

def squares():
    ints = integers()
    for i in ints:
        yield i ** 2

def take(n, iterator):
    j = 0
    array = []
    for i in iterator:
        if j >= n:
            break
        array.append(i)
        j += 1
    return array

print(take(5, squares()))
