class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=defaultdict(int)

        for num in nums:
            result[num]+=1

        sorted_dict=dict(sorted(result.items(),key=lambda item:item[1],reverse=True))
        return next(iter(sorted_dict))
        

        