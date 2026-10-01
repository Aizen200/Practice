class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        obj2={}
        ans=0
        l=0
        for r in range(len(s)):
            obj2[s[r]]=1+obj2.get(s[r],0)
            while (r-l+1)-max(obj2.values())>k:
                obj2[s[l]]-=1
                if obj2[s[l]]==0:
                    del obj2[s[l]]
                l+=1
            ans=max(ans,r-l+1)
        return ans

