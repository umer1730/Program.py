class Solution:
    def searchInsert(self,nums: list[int],target: int):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
x = Solution()
print(x.searchInsert([1,3,5,6], 5))    
print(x.searchInsert([1,3,5,6], 2))    
print(x.searchInsert([1,3,5,6], 7))    
print(x.searchInsert([1,3,5,6], 0))    
