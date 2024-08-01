def solution(letter):
    answer = ''
    morse = { 
    '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
    '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
    '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
    '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
    '-.--':'y','--..':'z'}
    #temp에 split함수를 사용하여 공백을 기준으로 나눔
    temp = letter.split(' ')
    #temp를 인덱스 형식으로 순회하면서 
    for i in temp:
        #morse 딕셔너리 key값이 모스부호니까 key값에 temp[i]의 value값을 넣으면 morse딕셔너리의
        #value값이 나온다. 그 값을 answer에 누적
        answer += morse[i]
    return answer