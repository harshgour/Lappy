def main():
    n=int(input("Enter N:"))
    k=int(input("Enter K:"))
    a=[*range(1,n+1,1)]
    i=k-1
    while(len(a)!=1):
        print(a)
        del a[i]
        i=i+k-1
        if i>len(a):
            i=i%len(a)
    print(a)
main()
