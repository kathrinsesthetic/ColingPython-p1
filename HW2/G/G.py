def solution(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        elif a[i] > b[j]:
            result.append(b[j])
            j += 1
        else:
            while j < len(b) and i < len(a) and a[i] == b[j]:
                j += 1
    if i < len(a):
        result += a[i:]
    elif j < len(b):
        result += b[j:]
    return result
