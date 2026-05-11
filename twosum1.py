nums = [3,2,4]
target = 6
n=len(nums)

def twosum(nums, target):
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
print(twosum(nums, target))