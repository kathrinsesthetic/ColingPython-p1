a = [[1,2,3], [4,5,6]]
a_rotate = tuple(zip(*a[::-1]))
def solution(a):
    for _ in a_rotate:
        print(list(_))

print(solution(a))

