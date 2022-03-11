def maxSubArraySum(a): 
    ans = a[0]
    cur = 0
    for i in range(len(a)):
        cur = cur + a[i]
        if cur < 0 :
            cur = 0

        elif ans < cur:
            ans = cur

    return ans
        
    
a = [-1,-2,-3,-4]
print ("Maximum contiguous sum is", maxSubArraySum(a))


#same algorithm but a bit differnet approach here we are setting ans's value = a[0]. and only updating it when the cur sum value is greater than it.