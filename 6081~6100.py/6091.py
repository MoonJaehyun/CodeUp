#6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)

a, b, c = input().split()
a, b, c= int(a), int(b), int(c)
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)