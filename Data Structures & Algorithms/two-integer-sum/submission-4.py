class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            check =  target-n
            if check in nums[i+1:]:
                return [i,nums.index(check,i+1)]
        