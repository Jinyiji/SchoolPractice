def solution(absolutes, signs):
    answer = 0
    for i in range(3):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


if __name__ == "__main__":
    abs = [4, 7, 12]
    s = [True, False, True]
    print(solution(abs, s))