T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    student_grade = list(list(map(int, input().split())) for _ in range(N))
    student_grade_sorted = sorted(student_grade, key=lambda x: (x[0] * 0.35) + (x[1] * 0.45) + (x[2] * 0.2), reverse= True)
    rating = student_grade_sorted.index(student_grade[K-1])
    cut_line = N // 10
    print(f"#{tc}", grade[rating//cut_line])