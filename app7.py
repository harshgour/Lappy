#class9
class A:
    def __init__(self,a):
        self.a=a
    def check(self):
        if self.a%2!=0:
            print("Weird")
        else:
            if self.a>=2 and self.a<=5:
                print("Not Weird")
            elif self.a>=6 and self.a<=20:
                print("Weird")
            else:
                print("Not Weird")
a=int(input(""))
x=A(a)
x.check()
