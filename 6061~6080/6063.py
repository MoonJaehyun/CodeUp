#6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)
a, b = input().split()
a = int(a)  #변수 a에 저장되어있는 값을 정수로 바꾸어 다시 변수 a에 저장
b = int(b)
c = (a if (a>=b) else b)
print(int(c))