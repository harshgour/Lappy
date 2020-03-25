a=list(map(int,input(" ").strip().split(" ")))
a.sort()
max=0
for i in range(len(a)-4,len(a)):
    max+=a[i]
print(f"{a[0]+a[1]+a[2]+a[3]} {max}")
