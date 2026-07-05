class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        start = 0

        for color in range(3):  # 0, 1, 2
            nums[start:start + count[color]] = [color] * count[color]
            start += count[color]


        
        