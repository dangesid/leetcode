s = "hello"
lst = []
for i in range(0,len(s)-1):
    diff = abs(ord(s[i])-ord(s[i+1]))
    print(diff)
    lst.append(diff)
print(sum(lst))
