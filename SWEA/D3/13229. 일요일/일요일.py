T = int(input())
for tc in range(1,T+1):
    #요일 나타내는 문자열을 담은 리스트 SUN이 젤 마지막에 온다.
    s_list = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    #T만큼 s 문자열을 입력받아서
    s = input()
    #s가 해당하는 인덱스 번호를 s_list에서 찾아서 s_idx에 저장
    s_idx = s_list.index(s)
    #s_idx가 6이면 s가 SUN을 입력받은거기때문에
    if s_idx == 6:
        #그 다음날 즉 MON부터 SUN까지 길이를 구하는것이니까 len(s_list)를 출력
        print('#'+str(tc), len(s_list))
    #다른 요일이면 SUN의 인덱스 번호보다 작으니까 s_list길이에서 s_idx+1을 한 값을
    #빼줌
    else:
        print('#'+str(tc), len(s_list) - (s_idx+1))