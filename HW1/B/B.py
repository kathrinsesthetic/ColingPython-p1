n = int(input('n = '))

def solution(n):
    head = '    _~_    '
    eyes = '   (o o)   '
    mouth = '  /  V  \  '
    belly = ' /(  _  )\ '
    legs = '   ^^ ^^   '
    print(head*n, end='\n')
    print(eyes*n, end='\n')
    print(mouth*n, end='\n')
    print(belly*n, end='\n')
    print(legs*n, end='\n')

print(solution(n))
