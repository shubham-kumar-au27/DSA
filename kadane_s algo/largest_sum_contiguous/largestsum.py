def maxSubArraySum(a):
    ans = -10**8
    cur = 0
    for i in range(len(a)):
        cur = cur + a[i]
        if cur > ans:
            ans = cur
        if cur < 0 :
            cur = 0
    return ans

a = [-1,-2,-3,-4]
print ("Maximum contiguous sum is", maxSubArraySum(a))
 

#logic of this algorithm is that if every elemnt of the array is positive then there is no need visit the element twice because in that case the biggest contigous sum will be the sum of all array. 
#And when ever we will find the cur sum < 0. then there is no need to add it from  the next element because it will only lower our total sum. so we start from 0 when ever we find the sum negative.
