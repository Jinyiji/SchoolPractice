def solution(price, grade):
    # 코드 작성 공간
# "S" : 5%, "G" : 10%, "V" : 15%
    if grade = "S" :
        return price - price*0.05
    if grade == "G" :
        return  price - price*0.10
    if grade = "V":
        return price - price * 0.15

#testcase를 위한 output
price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)
print("ret1 = ")

# 2.2/3 , 4/23일에 대해
def 보조함수(mouth, day):
    mouth_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
     for i in range(mouth -1):
         total += mouth_list[i]
    total += @@@
    return total - 1

def solution(start_mouth, start_day, end_mouth, end_day):
    start_total = 보조함수(start_mouth, start_day)
    end_total = 보조함수(end_mouth, end_day)
    return end_total - start_total