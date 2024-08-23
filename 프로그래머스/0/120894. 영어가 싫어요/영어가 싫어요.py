def solution(numbers):
    #zeroe 부터 nine까지의 temp_list를 하나 만든다.
    temp_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    #enumerate함수를 사용하여 temp_list의 index와 value값을 다 가져와서 순회
    for i, v in enumerate(temp_list):
        #replace함수를 사용하여 temp_list의 v값(value)값을 str형식의 i로 바꿔줌
        numbers = numbers.replace(v , str(i))
    #str형식의 numbers를 int형식으로 형 변환을 해준 뒤 리턴
    return int(numbers)