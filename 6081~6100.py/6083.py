#6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
r,g,b=map(int, input().split())
for i in range(r):

    for j in range(g):

        for k in range(b):

            print(i,j,k)

print(r*g*b)
