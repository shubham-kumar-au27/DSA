from cmath import inf
#This is a brute force solution where we are taking nested loops to get the solution and the time complexity for this code is o(n^2).
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
#methods used --- In this method we have iterate through every list of element twice.. once by fixing the i the element and checking the sum with every sub elements for ex - [-5,4,6,-3,4,-1].
# in this we will fix -5 and check the sum with every remaining elements like this  (-5+4)=-1 -- (-1+6) = 5 -- (5+(-3)) = 2 -- to (n-1) in the same way 4+6 -- (10 +(-3)) ... to (n-1)
#in order to do this I am iterating every element of i in add and adding it to the next element by fixing the i the element and every time i am adding the next element i am checking it with another variable sum..if the elemnt is greater than the elements seen till now then we are updating the variable and at last we get the sol for the largest sum. 

    
            
        


nums = [-5,4,6,-3,4,-1]

res = largestsum(nums)

print(res)
