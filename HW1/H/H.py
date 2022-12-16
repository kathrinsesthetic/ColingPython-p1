def solution(a):
    result = list(zip(a[0], a[1]))
    i = 0
    for row in result:
        result[i] = list(row)
        i += 1
    for row in a[2:]:
        i = 0
        for el in zip(result, row):
            result[i] = list(el)
            i += 1
        i = 0
        for p in result:
            p[0].append(p[1])
            result[i] = p[0]
            i += 1
    return result


