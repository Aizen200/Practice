class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r=max(weights),sum(weights)
        ans=float('inf')
        while l<=r:
            m=(l+r)//2
            add=0
            count=1
            for i in weights:
                if add+i>m:
                    count+=1
                    add=i
                else:
                    add+=i
            if count<=days:
                ans=min(ans,m)
                r=m-1
            elif count>days:
                l=m+1
        return ans