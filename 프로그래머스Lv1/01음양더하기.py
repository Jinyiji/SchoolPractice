def solution(absolutes, signs):
    answer = 0
    if signs[0] == True:
        answer += absolutes[0]
    else:
        answer -= absolutes[0]

    if signs[1] == True:
        answer += absolutes[1]
    else:
        answer -= absolutes[1]

    if signs[2] == True:
        answer += absolutes[2]
    else:
        answer -= absolutes[2]
    return answer


if __name__ == "__main__":
    abs = [4, 7, 12]
    s = [True, False, True]
    print(solution(abs, s))
