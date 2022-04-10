def replaceElements(arr1):
    ans = [0]*len(arr1)
    for i in range(len(arr1)-2, -1, -1):
        ans[i] = max(ans[i+1],arr1[i+1])
    return ans
arr = [17,18,5,4,6,1]
print(replaceElements(arr))
