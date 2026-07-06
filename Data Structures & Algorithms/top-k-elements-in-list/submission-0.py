class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)

        for num in nums:
            dic[num]+=1

        sorted_dic = {k:v for k, v in sorted(dic.items(),key=lambda item:item[1],reverse=True)} 

        result=[]

        for index,(key,value) in enumerate(sorted_dic.items()):
            if index==k:
                break
            result.append(key)
        return result