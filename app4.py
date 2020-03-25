n=list(map(int,input(" ").strip().split(" ")))
a=list()
b=list()
c=list()
for i in range(n[0]):
    x=list(map(int,input(" ").strip().split(" ")))
    a.append(x[0])
    b.append(x[1])
    c.append(x[2])
p=int(input(" "))
if p==0:
    for i in range(n[0]):
        for j in range(n[0]-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j]=temp
                temp=c[j]
                c[j]=c[j+1]
                c[j]=temp
                temp=b[j]
                b[j]=b[j+1]
                b[j]=temp
elif p==2:
    for i in range(n[0]):
        for j in range(n[0]-i-1):
            if c[j]>c[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j]=temp
                temp=c[j]
                c[j]=c[j+1]
                c[j]=temp
                temp=b[j]
                b[j]=b[j+1]
                b[j]=temp
elif p==1:
    for i in range(n[0]):
        for j in range(n[0]-i-1):
            if b[j]>b[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j]=temp
                temp=c[j]
                c[j]=c[j+1]
                c[j]=temp
                temp=b[j]
                b[j]=b[j+1]
                b[j]=temp

for i in range(n[0]):
    print(f"{a[i]} {b[i]} {c[i]}")
