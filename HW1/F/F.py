def solution(n):
    k = 1
    result = []
    while k <= n:
        result.append(k)
        k *= 2
    return result