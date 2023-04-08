#  문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 숫자(0~9)와 소수점(.)을 사용해 표현한 수를 실수(real number)라고 한다.

# 변수에 실수값을 저장한 후
# 변수에 저장되어 있는 값을 그대로 출력해보자.

# 예시
# f = input()
# f = float(f)
# print(f)
# 와 같은 형태로 가능하다.

# 참고
# 어떤 값을 1개 입력받아 계산하거나 처리해야하는 경우라면, 입력되는 값이 수인지 문자열인지 구분해야한다.
# 조금 생각해보면, 키보드로 입력한 9라는 값이 문자 9인지, 정수 9인지, 실수 9.0인지 컴퓨터가 스스로 구분하지 못한다는 것을 알 수 있다.
# 컴퓨터 내부에서는 2진 체계의 디지털 형태로만 저장할 수 있기 때문에 정수, 문자, 실수 등의 저장 방법이 다르다.
# 입력한 값을 원하는 형태로 계산하거나 처리하기 위해서는 입력한 값이 어떤 데이터(정수, 문자, 실수, 문자열 등)인지 명확히 구분해 주어야 한다.
f = input()
f = float(f)
print(f)