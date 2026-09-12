class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"/"+i
        return s

    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        while i<len(s):
            temp=i
            while s[temp]!="/":
                temp+=1
            length=int(s[i:temp])
            ans.append(s[temp+1:temp+1+length])
            i=temp+1+length
        return ans
            
