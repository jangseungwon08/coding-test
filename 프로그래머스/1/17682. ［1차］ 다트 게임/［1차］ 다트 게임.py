def solution(dartResult):
    res = []
    point = []
    dart_point = {'S':1 , 'D': 2, 'T':3}
    temp_str = dartResult[0]
    for i in range(1,len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '0' and temp_str == '1':
                temp_str += dartResult[i]
            else:
                res.append(temp_str)
                temp_str = dartResult[i]
        else:
            temp_str += dartResult[i]
    res.append(temp_str)
    for i in range(len(res)):
        dart = res[i]
        num_str = ""
        bonus = ''
        option = ''
        for char in dart:
            if char.isdigit():
                num_str += char
            elif char in dart_point:
                bonus = char
            else:
                option = char
        num = int(num_str) ** dart_point[bonus]
        if option == '*':
            num *= 2
            if i> 0:
                point[i-1] *= 2
        elif option == '#':
            num *= -1
        point.append(num)
    print(sum(point))
    return sum(point)