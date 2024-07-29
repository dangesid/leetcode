arr = [2,3,5,1,3]
extra = 3
arr_2 = []
arr_3 = []
for i in range(0,len(arr)):
    ele = arr[i]+extra
    arr_2.append(ele)

for i in range(len(arr_2)):
    if arr_2[i]>= max(arr):
        arr_3.append(True)
    else:
        arr_3.append(False)
print(arr_3)
