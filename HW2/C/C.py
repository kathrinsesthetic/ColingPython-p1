def solution(arr):
    top, left = -1, -1
    right = len(arr[0])
    bottom = len(arr)
    i, j = 0, 0
    result = []
    while right - left > 1 and bottom - top > 1:
        while j < right:
            result.append(arr[i][j])
            j += 1
        top += 1
        if bottom - top == 1:
            break
        j -= 1
        i += 1
        while i < bottom:
            result.append(arr[i][j])
            i += 1
        right -= 1
        if bottom - top == 1:
            break
        i -= 1
        j -= 1
        while j > left:
            result.append(arr[i][j])
            j -= 1
        bottom -= 1
        if bottom - top == 1:
            break
        j += 1
        i -= 1
        while i > top:
            result.append(arr[i][j])
            i -= 1
        left += 1
        if bottom - top == 1:
            break
        i += 1
        j += 1
    return result
