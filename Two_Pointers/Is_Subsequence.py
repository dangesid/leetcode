s = "abc"
t = "ahbgdc"
n1 = len(s)
n2 = len(t)
p1 = 0
sub = ""

for i in range(n1):
    print(p1,n2)
    for j in range(p1,n2):
        if s[i] == t[j]:
            sub += s[i]
            p1 = j+1
            break
    print(sub)
if sub:
    print(True)
