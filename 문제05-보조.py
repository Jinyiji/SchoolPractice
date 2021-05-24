# 해당하는 숫자는 박수를 몇 번 쳐야 하는가?

a = 613

카운터 = 0

for num in range(1, a+1):
while num:
    if num % 10==3 or num%10==6 or num%10==9:
        카운터 += 1
    num = num // 10

print(카운터)