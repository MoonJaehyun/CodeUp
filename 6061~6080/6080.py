#6080 : [기초-종합] 주사위 2개 던지기(설명)(py)
n, m = input().split()
n, m = int(n), int(m)
for i in range(1, n+1) :
  for j in range(1, m+1) :
    print(i, j)