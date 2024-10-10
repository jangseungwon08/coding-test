N = int(input())
#초기값 가로길이 세로길이 state(점의 수) 초기값 설정
length , width , state = 2, 2, 0
#N이 1일때는 1을 더하여 3*3을 출력하니 length와 width에 1을 더해줘서 곱한값을 출력
if N == 1:
    state = (length +1) * (width+1)
    print(state)
#N이 2 이상일때
else:
    #i 1부터 N까지 순회하면서
    for i in range(1,N+1):
        #i가 1일때는 아까 N이 1일때의 조건문과 동일하게 더해줌
        if i == 1:
            length += i
            width += i
        #length의 값이 2 3 5 9 17 33으로 길이가 초기값에서 3으로 넘어갈 때만
        #1이 증가하고 그 후로는 2의 제곱만큼 길이가 증가하여 2부터는 2의 제곱만큼
        #2의 i제곱만큼 길이와 폭에 더해줘서 그 두개의 값을 곱함
        else:
            length += 2**(i-1)
            width += 2**(i-1)
    state = length * width
    print(state)