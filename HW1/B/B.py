n = int(input('n = '))

def solution(n):
    if n == 0:
        return ""
    head =  '   _~_   '
    eyes =  '  (o o)  '
    mouth = ' /  V  \ '
    belly = '/(  _  )\\'
    legs =  '  ^^ ^^  '
    result = head*n + '\n'
    result += eyes*n + '\n'
    result += mouth*n + '\n'
    result += belly*n + '\n'
    result += legs*n
    return result