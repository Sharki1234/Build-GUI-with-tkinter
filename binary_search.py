def binary_search():
    nums = [0,1,2,3,4,5,6]
    target = 4
    i = 0
    j = (len(nums))-1
    mid = 0
    found = False
    while i<=j:
        mid = (i+j)//2
        if nums[mid] == target:
            print("found it!!")
            break
        elif nums[mid] > target:
            j = mid-1
            
        
            
            
        elif nums[mid] < target :
            #i != len(nums)
            i = mid+1
            
        
    if i>j:
        print("not found")
        
binary_search()