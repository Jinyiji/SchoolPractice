# 1 letters 가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# letters = 'python'
# lang = 'python'
# print(lang[0], lang[2])


# 2 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# license_plate = "24가 2210"
# print(license_plate [4:])


# 3 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# phone_number = "010-1111-2222"
# phone_number1 = phone_number.replace("-", " ")
# print(phone_number1)


# 4 url 에 저장된 웹 페이지 주소에서 끝 글자만 출력하시오.
# url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])


# 5 변수에 다음과 같은 문자열이 바인딩되어 있습니다. 번갈아가면서 출력하라.
# t1 = 'python'
# t2 = 'java'
# print((t1 + ' ' + t2 + ' ')*4)


# 6 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",", "")
# 타입변환 = int(컴마제거)
# print(타입변환, type(타입변환))


# 7 다음과 같이 문자열이 있을 때 btc 와 krw 로 나눠보세요.
# ticker = "btc_krw"
# a = ticker.split('_')
# print(a)


# 8 movie_rank = ["닥터 스트레인지", "스플릿", "럭키"] 리스트에 "배트맨"을 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
# movie_rank.append("배트맨")
# print(movie_rank)


# 9 movie_rank 리스트에 "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)


# 10 movie_rank 리스트에서 '럭키' 를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# del movie_rank[3]
# # movie_rank.remove("럭키")
# print(movie_rank)


# 11 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# print(sum(nums))


# 12 다음 리스트에 저장된 데이터의 개수를 화면에 구하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
# print(len(cook))


# 13 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# print(sum(nums)/len(nums))


# 14 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])

# 15 interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용, 출력.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print('/'.join(interest))


# 16 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# string = "삼성전자/LG전자/Naver"
# interest = [string[0:4], string[5:9], string[10:15]]
# print(interest)


# 17 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]
# data.reverse()
# a = sorted(data)
# print(a)


# 18 사용자로부터 입력 받은 시간이 정각인지 판별하라.
# a = "02:00"
# result = a.split(":")
#
# if result[-1] == "00":
#     print("정각입니다.")


# 19 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for x in 리스트:
#     if x.split('.')[-1] == 'h':
#         print(x)


# 20 for 문을 사용해서 0.0, 0.1 ... 0.9 출력
# for i in range(9+1):
#     print(str(0.1 * i)[:3])


# 21 리스트에 저장된 데이터를 출력
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# apart = [[101, 102], [201, 202], [301, 302]]
# for x in apart:
#     # print(x)
#     for y in x:
#         print(f"{y} 호")


# 22 숫자로 구성된 하나의 리스트를 입력받아,
# 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# def pickup_even(arr):
#     result = list()
#     for x in arr:
#         if x % 2 == 0:
#             result.append(x)
#     return result
# a = pickup_even([3, 4, 5, 6, 7, 8])
# print(a)