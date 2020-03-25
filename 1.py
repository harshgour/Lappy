import math
class square:
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)
class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
class circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        print(math.pi*self.r*self.r)
class triangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(1/2*self.l*self.b)
def calc(shape):
    shape.area()
def main():
    obj1=square(2)
    obj2=rect(2,3)
    obj3=circle(2)
    obj4=triangle(2,2)
    calc(obj1)
    calc(obj2)
    calc(obj3)
    calc(obj4)
main()
"""method overloading"""

"""class A:
    def hi(self,name=None):
        print("Hello {0}".format(name))
    def hi(self,name,last):
        print("Hello {} {}".format(name,last))
def x():
    obj1=A()
    obj1.hi("harsh")
    obj1.hi("harsh","gour")
x()"""

def hi(self,name):
    print(name)
def hi(self,name,last):
    print(name,last)
hi("harsh")
hi("harsh","gour")
