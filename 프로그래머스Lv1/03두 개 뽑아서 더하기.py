# 정수 배열 numbers가 주어집니다.
# numbers에서 서로 다른 인덱스에 있는
# 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를
# 배열에 오름차순으로 담아 return 하도록
# solution 함수를 완성해주세요.

def solution(numbers):
    answer = list()
    # numbers[i]는 첫 번째로 뽑은 숫자
    # numbers[j]는 두 번째로 뽑은 숫자
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            value = numbers[i] + numbers[j]
            # 두 수를 뽑아 더한 값이 기존에 존재하지 않을 때
            if value not in answer:
                # list에 추가
                answer.append(value)
    # 오름차순으로 정렬
    answer.sort()
    return answer

def main():
    numbers = [5, 0, 2, 7]
    print(solution(numbers))


if __name__ == "__main__":
    main()