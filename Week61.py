from pyDatalog import pyDatalog
pyDatalog.create_terms('X, big, small, black, brown, gray, dark')

+big('Bear')
+big('Elephant')
+small('Cat')
+black('Cat')
+brown('Bear')
+gray('Elephant')


dark(X) <= black(X) 
dark(X) <= brown(X)

print(dark(X))
