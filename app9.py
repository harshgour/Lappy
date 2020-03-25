#class4
from functools import reduce
class A:
    def __init__(self,N,D):
        self.n=N
        self.d=D
    def num(self):
        return reduce(lambda i,j : i*j, self.n)
    def den(self):
        return reduce(lambda i,j : i*j, self.d)
    def red(self):
        redN = 0
        redD = 0 
        for i in range(2,min([self.num(),self.den()])):
            if self.num() % i == 0 and self.den() % i == 0:
                redN = self.num()//i
                redD = self.den()//i
        print(redN, redD)

s = int(input())
N = list()
D = list()
for i in range(s):
    (x,y) = map(int, input().split())
    N.append(x)
    D.append(y)
x=A(N,D)
x.red()
