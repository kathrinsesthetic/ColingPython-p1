def solution(arr):
    interval, max_interval = 1, 0
    i = 0
    while i < (len(arr)):
        while i + 1 < (len(arr)) and arr[i] == arr[i + 1]:
            interval += 1
            i += 1
        if interval > max_interval:
            max_interval = interval
        interval = 1
        i += 1
    return max_interval
