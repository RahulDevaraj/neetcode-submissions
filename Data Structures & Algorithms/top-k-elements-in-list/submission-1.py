class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]

        for num in nums:
            count[num]+=1

        for num, cou in count.items():
            freq[cou].append(num)

        result=[]
        for i in range(len(freq)-1,0 ,-1):
            for item in freq[i]:
                if len(result)<k:
                    result.append(item)
        return result



        
        
        