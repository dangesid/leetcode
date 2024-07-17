# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

arr = [0, 1, 0, 3, 12]


non_zero_index  = 0
for i in range(0,len(arr)):
    if arr[i]!= 0:
        arr[i],arr[non_zero_index] = arr[non_zero_index],arr[i]
        non_zero_index+=1
print(arr)