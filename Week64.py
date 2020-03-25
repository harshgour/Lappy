from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y, marks, passm')

+marks('DEVANG',90)
+marks('AKSHAT',75)
+marks('AHMED', 2)
+marks('HARSH', 60)
+marks('RAJ',80)
a=input()
'''if( marks(a,Y) & (50<=Y)):
    print(f"Passed!!")
else:
    print("Failed!!")'''
pr
passm(X,Y) <= marks(X,Y) & (50 <= Y)
#print(f"Passed students are {passm(X,Y)}")
