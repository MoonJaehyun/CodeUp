#6087 : [기초-종합] 3의 배수는 통과(설명)(py)
n = int(input())

for i in range(1, n+1) :
  if i%3==0 :
    continue            #다음 반복 단계로 넘어간다.
  print(i, end=' ')    #i가 짝수가 아닐 때만 실행된다.