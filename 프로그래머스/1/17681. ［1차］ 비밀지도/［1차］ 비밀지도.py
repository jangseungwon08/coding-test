def solution(n, arr1, arr2):
    answer = []
    #임시 리스트
    temp_arr= []
    #n인 정사각형이니까 n만큼 돌림
    for i in range(n):
        #bin함수를 사용하여 arr1과 arr2를 0b형식의 이진수로 나타내서 temp_arr에 append
        temp_arr.append(bin(arr1[i] | arr2[i]))
        #n의 크기만큼 이진수가 안나올 수도 있으니              
        #n != len(temp_arr[i][2:]) 의 값이 true일 때만 
        while n != len(temp_arr[i][2:]):
            #i번째 2진수 값을 list형식으로 바꿔줌 ->시간복잡도 아낌
            temp_arr[i] = list(temp_arr[i])
            #젤 앞에 붙여야하므로 b뒤에 붙임
            temp_arr[i][1] += '0'
            #''.join을 사용하여 temp_arr[i]길이 업데이트
            temp_arr[i] = ''.join(temp_arr[i])
            #이 while문은 temp_arr[i]의 길이가 n과 같아질때까지 '0'값을 추가함
    #temp_arr for문 돌리면서
    for j in temp_arr:
        #임시 문자열
        temp_str = ''
        #temp_arr의 각 원소 문자열들이 0b로 시작하기때문에 2부터 len(j)-1번째 인덱스까지
        for k in range(2, len(j)):
            #문자열 j의 각 원소값이 1이면
            if j[k] == '1':
                #temp_str에 '#'추가
                temp_str += '#'
                #각 원소값이 0이면
            elif j[k] == '0':
                #공백 추가
                temp_str += ' '
        #temp_arr에 있는 하나의 원소 문자열을 다 돌았으면 temp_str을 append로 붙여줌
        answer.append(temp_str)
    return answer