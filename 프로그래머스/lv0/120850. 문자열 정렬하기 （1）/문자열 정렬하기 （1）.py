def solution(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            pass
    return sorted(answer)