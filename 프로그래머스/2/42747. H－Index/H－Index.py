def solution(citations):
    citations = sorted(citations, reverse=True)
    for i,v in enumerate(citations):
        if i+1 > v:
            return i
    return len(citations)