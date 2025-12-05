nums = [0,1,2,3,4,5,6]
target = 5
i = 0
j = len(nums)
mid = 0
found = False
while not found:
    mid = (i+j)//2
    if nums[mid] == target:
        print("found it!!")
        found = True
    elif nums[mid] > target:
        j = mid
        print("hi")
        
    elif nums[mid] < target:
        i = mid
        print("hello")


