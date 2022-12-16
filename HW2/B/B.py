def solution(x):
    lastOcc = 0
    i = 0
    first_h = 1
    deleted_h = 0
    result = ""
    while i < len(x):
        if i % 3 == 0 and i != 0:
            if x[i] == 'h':
                first_h = 0
                deleted_h = len(result) - 1
            i += 1
            continue
        elif x[i] == '1':
            result += "one"
        elif x[i] == 'h':
            if first_h:
                first_h = 0
                result += 'h'
            else:
                result += 'H'
                lastOcc = len(result) - 1
        else:
            result += x[i]
        i += 1
    if lastOcc > deleted_h:
        result = result[:lastOcc] + 'h' + result[lastOcc + 1:]
    return result