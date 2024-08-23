def solution(my_string):
    answer = []
    #대문자 A부터 소문자 z까지 52개 문자를 딕셔너리로 만듬
    temp_dic = {'A' : 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0, 'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    #my_string문자열 순회 하면서
    for i in my_string:
        #i가 temp_dic에 있으면
        if i in temp_dic:
            #temp_dic[i] -> temp_dic의 key를 i로 가지는 value값 1 증가
            temp_dic[i] += 1
    #temp_dic.values 순회 하면서
    for j in temp_dic.values():
        #하나씩 answer에 저장
        answer.append(j)
    return answer