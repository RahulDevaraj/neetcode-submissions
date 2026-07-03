class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=defaultdict(int)

        for num in nums:
            result[num]+=1

        return max(result, key=result.get)
        

        