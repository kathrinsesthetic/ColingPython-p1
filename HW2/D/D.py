def solution(n,k):
    i = 1
    result = 1
    while i < n:
        result = (result + k - 1) % (i + 1) + 1
        i += 1
    return result
