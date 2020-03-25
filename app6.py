#class6
s = input()
stuart = 0
kevin = 0
s2 = list()
s3 = list()
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        s3.append(s[i:j])
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if s[i:j] not in s2:
            s2.append(s[i:j])
            if s[i] in 'AEIOUaeiou':
                kevin+=s3.count(s[i:j])
            else:
                stuart+=s3.count(s[i:j])
print(stuart)
/Users/harshgour/Documents/app2.py
