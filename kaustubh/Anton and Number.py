a,b,c,d = map(int, input().split())
s = 0
x,y,z,v = 0,0,0,0
while x<a:
        s+=256
        x+=1
        z+=1
        v+=1
while y < b and x < a:
        s+=32
        y+=1
        x+=1
print(s)