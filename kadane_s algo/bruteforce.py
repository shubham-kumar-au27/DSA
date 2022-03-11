from cmath import inf


def largestsum(nums):

    sum = -(inf)
    add = 0

    for i in range(len(nums)):
        add = nums[i]
        for j in range(i+1,len(nums)):
            add += nums[j]
            if add > sum:
                sum = add

    return sum

    
            
        


nums = [-5,4,6,-3,4,-1]

res = largestsum(nums)

print(res)
