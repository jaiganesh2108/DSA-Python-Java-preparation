class removeDuplicate:
    def removeduplicate(self, nums):
        seen = set()
        index = 0

        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[index] = nums[i]
                index += 1
        return index
    
obj = removeDuplicate()
nums = [1, 1, 2]
k = obj.removeduplicate(nums)
print("Unique elements:", nums[:k])