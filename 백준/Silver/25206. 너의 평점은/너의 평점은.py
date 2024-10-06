#grade를 받기위한 grade의 형식을 dict형태로 초기화
grade_dict = {'A+':	4.5,
'A0':	4.0,
'B+':	3.5,
'B0':	3.0,
'C+':	2.5,
'C0':	2.0,
'D+':	1.5,
'D0':	1.0,
'F'	:0.0}
#전공 평점의 총합을 위한 total_grade
total_grade = 0
#학점의 총합을 위한 total_grade_num
total_grade_num = 0
#20개 까지 입력받으니까 0부터 19까지 for문 순회
for i in range(20):
    #입력값이 3개여서 s와 grade_num grade로 나눔
    s , grade_num , grade = input().split()
    #grade의 문자열 값이 P이면 total_grade_num에 0 추가(p인과목은 계산에서 제외)
    if grade == 'P':
        total_grade_num += 0
    else:
        #전공 학점을 float형식으로 형 변환 후 입력받은 grade값을 grade_dict의 key값으로 value값을 곱합
        total_grade += float(grade_num) * grade_dict[grade]
        #학점의 총합을 입력받은 grade_num을 float형식으로 형 변환하여 total_grade_num으로 누적 합
        total_grade_num += float(grade_num)
        #전공 평점 총합 나누기 학점 총합을 나눠서 소수점 6자리 까지 출력
print(round(total_grade / total_grade_num, 6))
