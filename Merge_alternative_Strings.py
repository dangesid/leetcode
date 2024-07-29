word1 = "ab"
word2 = "pqrs"

str_1 = ""
list = []

max_len = max(len(word1),len(word2))

for i in range(max_len):
    if i < len(word1):
        list.append(word1[i])
    if i < len(word2):
        list.append(word2[i])

merged_string = "".join(list)
print(merged_string)