import random

nums = [random.randint(0,50) for i in range(10)]
print(nums)

def merge(start1,end,mid,lis):
    start2 = mid+1
    extra = []
    p = start1
    
    while start1<=mid and start2<=end:
        #print(p,start1,start2)
        if lis[start1]<lis[start2]:
            extra.append(lis[start1])
            start1+=1
        else:
            extra.append(lis[start2])
            start2+=1
    while start1<=mid:
        extra.append(lis[start1])
        start1+=1
    while start2<=end:
        extra.append(lis[start2])
        start2+=1
    print(extra)
    k = 0
    for i in range(p,end+1):
        nums[i] = extra[k]
        k+=1

def mergesort(i,j,lis):
    if i<j:
        # i = 0
        # j = len(nums)-1
        mid = (i+j)//2
        mergesort(i,mid,lis)                                                 
        mergesort(mid+1,j,lis)
        merge(i,j,mid,lis)
    
mergesort(0,len(nums)-1,nums)
#print(nums)
