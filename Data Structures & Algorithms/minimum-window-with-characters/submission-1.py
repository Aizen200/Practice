class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return""
        obj1,obj2={},{}
        ans,pos=[-1,-1],float('inf')
        l=0
        for i in t:
            obj1[i]=1+obj1.get(i,0)
        have,need=0,len(obj1)
        for r in range(len(s)):
            temp=s[r]
            obj2[temp]=1+obj2.get(temp,0)
            if temp in obj1 and obj2[temp]==obj1[temp]:
                have+=1
            while have==need:
                if (r-l+1)<pos:
                    ans=[l,r]
                    pos=(r-l+1)
                obj2[s[l]]-=1
                if s[l] in obj1 and obj2[s[l]]<obj1[s[l]]:
                    have-=1
                l+=1
        start,end=ans
        if pos==float('inf'):
            return ""
        else:
            return s[start:end+1]
