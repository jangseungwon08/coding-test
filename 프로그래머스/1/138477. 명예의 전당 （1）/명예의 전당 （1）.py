def solution(k, score):
    answer = []
    honest_k = []
    #score의 인덱스 범위만큼 for문 
    for i in range(len(score)):
        #명예의 전당 리스트 길이가 k값 보다 작으면
        if k > len(honest_k):
            #명예의 전당 리스트에 score[i] 값 추가
            honest_k.append(score[i])
            #내림차순으로 나타내기 위해서 sort함수 이용
            honest_k.sort(reverse=True)
            #append함수 이용하여 honest_k[-1]가장 마지막에 있는(가장 작은 값) 추가
            answer.append(honest_k[-1])
            #k값보다 명예의 전당 길이가 길어지면
        else:
            #score[i]번째 value값이 honest_k[-1]의 마지막 값 보다 크면
            if score[i] > honest_k[-1]:
                #마지막 값 제거하고
                honest_k.remove(honest_k[-1])
                #score[i]값 추가
                honest_k.append(score[i])
                #추가한 뒤 내림차순 정렬
                honest_k.sort(reverse=True)
                #answer값에 honest_k중에 가장 작은 값 추가
                answer.append(honest_k[-1])
                #score[i]가 honest_k[-1]값 보다 작으면
            else:
                #answer에 원래의 honest_k[-1]값 추가
                answer.append(honest_k[-1])
    return answer
