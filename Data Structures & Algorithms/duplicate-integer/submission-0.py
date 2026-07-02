class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_len=len(nums)
        set_len=len(list(set(nums)))
        if set_len!=original_len:
            return True
        return False
        