nums = [1,2,3,4,5]


arr = []
for i in range(len(nums)):
    if nums[i] %2 == 0:
        arr.append(nums[i])
        print(arr)

arr.remove(arr[0])
print(arr)