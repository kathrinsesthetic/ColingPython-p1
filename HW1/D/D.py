n = int(input('n = '))

def solution(n):
    hours = n // 60
    minutes = n % 60
    if hours <= 24:
        print(hours, minutes)
    elif hours > 24:
        hours = hours - 24
    
    

print(solution(n))
