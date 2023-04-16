#6098 : [기초-리스트] 성실한 개미(py)
m=[]
for i in range(12) :
  m.append([])
  for j in range(12) :
    m[i].append(0)

for i in range(10) :
  a=input().split()
  for j in range(10) :
    m[i+1][j+1]=int(a[j])

x = 2
y = 2
while True :
  if m[x][y] == 0 :
    m[x][y] = 9
  elif m[x][y] == 2 :
    m[x][y] = 9
    break

  if (m[x][y+1]==1 and m[x+1][y]==1) or (x==9 and y==9) :
    break

  if m[x][y+1] != 1 :
    y += 1
  elif m[x+1][y] != 1 :
    x += 1
    

for i in range(1, 11) :
  for j in range(1, 11) :
    print(m[i][j], end=' ')
  print()
#
# 1.먼저 입력을 array라는 리스트에 2차원 배열로 입력받습니다. 그리고 while 반복문을 사용합니다.
# while 반복문에서는 1. 현재 칸이 0이라면 9로 변환하고, 현재 칸이 2라면 9로 변환한 뒤 반복문을 종료시킵니다.
# 2. 오른쪽과 아래가 모두 1이라면 반복문을 종료시킵니다.
# 3. 오른쪽이 1이 아니라면 y를 증가시키고, 오른쪽이 1이고 아래쪽이 1이 아니라면 x를 증가시킵니다.
# 그리고 마지막에 이중 for 반복문으로 출력을 해주면 됩니다.
# 저는 왼쪽 가장 위 칸을 (0,0)으로 지정했고, 모범 답안에서는 (1,1)로 지정해서 코드가 살짝 다른 것 같습니다.

# 위와 같은 프로세스를 순서대로 따라가면서 코드를 구현하면 답을 구할 수 있습니다. 