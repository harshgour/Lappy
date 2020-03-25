class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,x): 
        print(f"{self.a+x.a}+{self.b+x.b}i")
    def __sub__(self,x):
        print(f"{self.a-x.a}+{self.b-x.b}i")
    def __mul__(self,x):
        print(f"{self.a*x.a-(self.b*x.b)}+{self.a*x.b+(self.b*x.a)}i")
    def mod(self):
        print(f"{(self.a*self.a+(self.b*self.b))**0.5}+0.00i")
    def __floordiv__(self,x):
        print(f"{(self.a*x.a+(self.b*x.b))/((self.a*self.a+(self.b*self.b))**0.5)}+{(self.b*x.a-(self.a*x.b))/((self.a*self.a+(self.b*self.b))**0.5)}i")
a=list(map(int,input("Enter C: ").strip().split(" ")))
b=list(map(int,input("Enter D: ").strip().split(" ")))
c=complex(a[0],a[1])
d=complex(b[0],b[1])
c+d
c-d
c*d
c//d
c.mod()
d.mod()
