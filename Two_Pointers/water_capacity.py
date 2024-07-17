height = [1,2,1]

max_area = 0
left = 0
right = len(height)-1

while left < right:
    width = right - left
    area = width * min(height[left],height[right])

    if area > max_area:
        max_area = area

    if height[left] < height[right]:
        left+=1
    else:
        right -= 1

print(max_area)