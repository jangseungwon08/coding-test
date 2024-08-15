def solution(bin1, bin2):
    answer = ''
    #이진수를 int형식 bin1 bin2로 만들어서 10진수의 숫자로 만들어준다.
    #int(bin2,2)하면 2진수에서 10진수로 바뀜
    bin1, bin2 = int(bin1,2), int(bin2,2)
    #answer에 다시 str형식으로 저장하기위해서 bin1과 bin2를 더한 값을 2진수로 변환 후 
    #슬라이싱을 사용하여 앞의 0b를 제거해준 뒤 str형 변환
    answer = str(bin(bin1+bin2))
    return answer[2:]