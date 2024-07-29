def gcd(str1, str2):
    if len(str2) == 0:
        return str1
    elif len(str1) < len(str2):
        return gcd(str2, str1)
    elif not str1.startswith(str2):
        return ""
    else:
        return gcd(str1[len(str2):], str2)

def find_gcd(str1, str2):
    return gcd(str1,str2)


str1 = "ABCABC"
str2 = "BCAABC"

print(find_gcd(str1,str2))
