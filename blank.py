nums = [1,2,3,4,5]
n = len(nums)
for i in range(n):
    flag = False
    for j in range((n-i)-1):
        if nums[j] > nums[j+1]:
            flag = True
            other = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = other
    # if not flag:
    #     break
    print(nums)
#print(nums)

