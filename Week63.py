from pyDatalog import pyDatalog
pyDatalog.create_terms('fact, N')

i = int(input())

fact[N] = N*fact[N-1] 
fact[1] = 1
 
print(fact[i]==N)
