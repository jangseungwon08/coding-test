def solution(nums):
    #가져갈 수 있는 폰켓몬 개수 take선언
    take = len(nums) // 2
    #해시로 풀기 위하여 phone_dict 딕셔너리 선언
    phone_dict = {}
    #nums순회하면서
    for i in nums:
        #딕셔너리는 고유한 key만 저장가능하기때문에 중복된 폰켓몬이 들어오면 값을 덮어쓴다.                   (중복제거) 여러개의 폰켓몬이 존재해도 딕셔너리에는 하나만 저장
        #phone_dict[i] = 1에서 i는 폰켓몬 종류이며, 이것이 해시 함수에 의해 해시된 후 딕셔너리              내의 특정 위치에 저장
        phone_dict[i] = 1
    #가져갈 수 있는 폰켓몬보다 phone_dict의 길이가 더 크면(많은 종류의 폰켓몬이 존재하면)
    if take <= len(phone_dict):
        #최대로 가져갈 수 있는 폰켓몬 take 리턴
        return take
   #take보다 적은 폰켓몬의 종류가 있으면 phone_dict길이 리턴
    return len(phone_dict)