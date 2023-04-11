#6043 : [기초-산술연산] 실수 2개 입력받아 나눈 결과 계산하기(py)
a, b =input().split()
a, b= float(a), float(b)
c = a/b
print( format(c, ".3f") )
