#내 풀이
"""
s_list = list(input().split())
temp1 = s_list[0][2]+ s_list[0][1] + s_list[0][0]
temp2 = s_list[1][2]+ s_list[1][1] + s_list[1][0]
if int(temp1) > int(temp2):
    print(temp1)
else:
    print(temp2)
    """
#num1 과 num2 를 공백을 기준으로 나눔
num1, num2 = input().split()
#num1은 num1에서 역순으로 출력하여 정수형으로 형 변환
num1 = int(num1[::-1])
#num2는 num2에서 역순으로 출력하여 정수형으로 형 변환
num2 = int(num2[::-1])
#num1이 num2보다 더 크면
if num1> num2:
    #역순으로 바꾼 num1 출력
    print(num1)
    #num2가 더 크면 역순으로 바꾼 num2 출력
else:
    print(num2)