def solution(date1, date2):
    #date1이 앞서는 날짜니까 28일이 29일보다 앞선다. 따라서 date1의 전체 slicing결과가              date2의 슬라이싱 결과보다 작으면 1을 리턴
    if date1[::] < date2[::]:
        return 1
    #date1의 슬라이싱 결과가 크거나 같으면 0리턴
    else:
        return 0
