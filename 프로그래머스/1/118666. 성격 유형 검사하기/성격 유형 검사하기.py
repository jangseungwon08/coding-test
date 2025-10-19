def solution(survey, choices):
    answer = ''
    p_dict = {"R":0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    for i in range(len(survey)):
        if choices[i] > 4:
            p_dict[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            p_dict[survey[i][0]] += 4 - choices[i]
        else:
            continue
    if p_dict["R"] >= p_dict["T"]:
        answer += "R"
    else:
        answer += "T"
    if p_dict["C"] >= p_dict["F"]:
        answer += "C"
    else:
        answer += "F"
    if p_dict["J"] >= p_dict["M"]:
        answer += "J"
    else:
        answer += "M"
    if p_dict["A"] >= p_dict["N"]:
        answer += "A"
    else:
        answer += "N"
    return answer