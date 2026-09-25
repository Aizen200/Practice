import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=float('inf')
        l,r=1,max(piles)
        while l<=r:
            hour=0
            m=(l+r)//2
            for i in piles:
                hour+=math.ceil(i/m)
            if hour>h:
                l=m+1
            elif hour<=h:
                ans=min(ans,m)
                r=m-1
        return ans

