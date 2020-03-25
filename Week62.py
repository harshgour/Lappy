#python -m pip install SomePackage
'''
from pyDatalog import pyDatalog
pyDatalog.create_terms('X,Y,Z,father,brother, cousin, grandson, descendent')

+father('devang','harsh')
+father('akshat','devang')
+brother('akshat','vividh')


descendent(X,Z) <=  father(Z,Y) & father(Y,X)
grandson(X,Y) <= father(X,Z) & father(Z,Y)
print(descendent(X,Z),grandson(X,Y))
'''
from pyDatalog import pyDatalog
pyDatalog.create_terms('W,X,Y,Z, father, brother, cousin, grandson, descendent')

+father('DEVANG','HARSH')

+father('DEVANG','AKSHAT')

+father('AKSHAT', 'AHMED')

+father('HARSH', 'VIVIDH')

+father('HARSH', 'RAJ')

brother(Y, Z) <= father(X, Y) & father(X,Z)
grandson(Z,X) <= father(X,Y) & father(Y,Z)
cousin(X,Y) <= father(Z,X) & father(W,Y) & brother(Z,W)
print(brother('HARSH',Y))
print(cousin('AHMED',Y))
