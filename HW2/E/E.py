def solution(a, b):
    if b == 1:
        return a + 1
    else:
        return solution(a, b - 1) + 1