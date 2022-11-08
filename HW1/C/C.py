n = int(input('n = '))
k = int(input('k = '))

def solution(n,k):
    a = k // n
    b = k % n
    print(a, b)

print(solution(n,k))
