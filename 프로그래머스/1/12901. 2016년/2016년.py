def solution(a, b):
    answer = ''
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    temp = sum(month[:a-1]) + b
    answer = day[temp % 7]
    return answer
