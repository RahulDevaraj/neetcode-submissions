class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res,i=[],0
        while i<len(s): 
            j=i           
            s_len=''
            while s[j]!='#':
                s_len+=s[j]
                j+=1
            i_len=int(s_len)
            res.append(s[j+1:j+1+i_len])
            i=(j+1+i_len)
        return res




