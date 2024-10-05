#문자열을 입력받아 리스트형식으로 만듬
s = list(input())
#반복문을 위한 알파벳 리스트 생성
alpha_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'
, 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#alpha_list순회하면서 
for i in alpha_list:
    #a부터 시작하여 a가 s에 존재하면 s의 i번째 인덱스 번호 출력
    #i번째 알파벳이 s에 존재하면
    if i in s:
        #문자열s에서 i의 알파벳 인덱스 번호를 출력 하고 한칸 띄우고 개행x
        print(s.index(i) , end = ' ')
        #문자열 s에 존재하지 않으면 -1출력하고 한칸 띄우고 개행 x
    else:
        print(-1 , end = ' ')
#이렇게 말고 find함수를 사용하여 문자가 문자열에 첫번째 위치한 순서를 숫자로 출력
