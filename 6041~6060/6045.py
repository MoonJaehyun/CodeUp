# 6045 : [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기(설명)(py)

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
abc = a+b+c
mean = abc/3
print(abc, format(mean, ".2f"))