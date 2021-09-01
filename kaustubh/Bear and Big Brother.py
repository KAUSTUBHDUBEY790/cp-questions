a,b = map(int, input().split())
c = 0
while a<=b:
    a,b,c=a*3,b*2,c+1
print(c)
