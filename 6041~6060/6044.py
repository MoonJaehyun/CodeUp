#6044 : [기초-산술연산] 정수 2개 입력받아 자동 계산하기(py)
a, b =input().split()
a, b= int(a), int(b)
c = a+b #합
d = a-b #차
e = a*b #곱
f = a//b #몫
g = a%b #나머지
h = a/b
#첫 번째 줄에 합
# 두 번째 줄에 차,
# 세 번째 줄에 곱,
# 네 번째 줄에 몫,
# 다섯 번째 줄에 나머지,
# 여섯 번째 줄에 나눈 값을 순서대로 출력한다.
# (실수, 소수점 이하 둘째 자리까지의 정확도로 출력)
print(c)
print(d)
print(e)
print(f)
print(g)
print( format(h, ".2f") )   