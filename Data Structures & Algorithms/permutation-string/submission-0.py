class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        obj1={}
        for i in s1:
            obj1[i]=1+obj1.get(i,0)
        l=0
        obj2={}
        for r in range(len(s2)):
            obj2[s2[r]]=1+obj2.get(s2[r],0)
            while (r-l+1)==len(s1):
                if obj1==obj2:
                    return True
                obj2[s2[l]]-=1
                if obj2[s2[l]]==0:
                    del obj2[s2[l]]
                l+=1
        return False