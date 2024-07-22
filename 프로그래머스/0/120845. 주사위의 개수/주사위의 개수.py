def solution(box, n):
    answer = 0
    #가로에 들어갈 n의 개수, 세로에 들어갈 n의 개수, 높이에 들어갈 n의 개수를 다 곱해주면 된다.
    answer = (box[0] // n)*(box[1]// n )*(box[2]//n)
    return answer