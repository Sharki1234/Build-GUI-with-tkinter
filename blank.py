def pr():   
    strs =["ab","a"]
    prefix = ""

    i = 0
    j = 0
    while True:
        if len(strs[i])==0:
             break
        if len(strs)==1:
            prefix+=strs[i]
            break
        if strs[i][j]==strs[i+1][j]==strs[i+2][j]:
                prefix+=strs[i][j]
                j+=1
        else:
            break
    return(prefix)
print(pr())