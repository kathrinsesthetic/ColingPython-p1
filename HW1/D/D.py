n = int(input('n = '))

def solution(n):
    minutes_in_day = 60 * 24
    n = n % minutes_in_day
    hours = n // 60
    minutes = n % 60
    return hours.__str__() + " " + minutes.__str__()
    
    

print(solution(n))
