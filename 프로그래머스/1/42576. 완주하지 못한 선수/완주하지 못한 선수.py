def solution(participant, completion):
    answer = ''
    #참가자이름을 key로 명수를 value로 하기위한 딕셔너리
    part_dict = {}
    #participant리스트를 순회
    for v in participant:
        #value값을 key값으로 하고 v에 해당하는 값을 가져온다. v가 part_dict에 없으면 기본적으로           0으로 시작하고 1을 더해줌
        part_dict[v] = part_dict.get(v, 0) + 1
        #completion순회하면서
    for i in completion:
        #part_dict[i]에 1을 빼줌
        part_dict[i] -= 1
        #part_dict[i]의 value값이 0이면
        if part_dict[i] == 0:
            #part_dict[i]를 제거
            del part_dict[i]
    #완주하고 남은 part_dcit의 key값을 for문 순회하면서 
    for i in part_dict.keys():
        #answer에 i를 누적저장 후 리턴
        answer += i
    return answer