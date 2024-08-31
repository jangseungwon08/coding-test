#파이썬에서 힙을 구현하기 위해 heapq import
import heapq

def solution(scoville, K):
    answer = 0
    #heapify를 사용하여 리스트 형식인 scoville을 힙 으로 변환해줌
    heapq.heapify(scoville)
    #scoville의 길이가 2 이상일때만(원소가 두개 이상일 때만 하나만 있으면 연산이 안됨)
    while len(scoville) >= 2:
        #가장 작은 원소를 scoville에서 heappop를 이용하여 min_1에 리턴 후 삭제한다.
        min_1 = heapq.heappop(scoville)
        #뽑은 min_1의 값이 기준 값 k보다 크면
        if min_1 >= K:
            #음식을 안섞어도 되니까 answer는 0이 된다.
            return answer
        #min_1의 값이 k보다 작으면
        else:
            #두번째 안매운 음식을 heappop를 이용하여 min_2에 리턴 후 삭제
            min_2 = heapq.heappop(scoville)
            #heappush를 통해 scoville 0번째 인덱스에 섞은 음식의 스코빌 지수 연산을                하여 첫번째 자리에 저장
            heapq.heappush(scoville, min_1+(min_2*2))
            #push연산을 하였으니 섞었다는 뜻이므로 answer 1 증가
            answer += 1
    #while문이 다 끝나고 scoville합이 K보다 작으면
    if sum(scoville) < K:
        #모든 음식의 스코빌 지수를 K이상으로 만들 수 없는 경우니까 -1 리턴
        return -1
    return answer