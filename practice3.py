nums = [2,7,3]
target = 9
map = {

}
answer = []
for i in range(len(nums)):
    if (target - nums[i]) in map:
        answer.append(i)
        answer.append(map[target-nums[i]])
    else:
        map[nums[i]]=i
print(answer)