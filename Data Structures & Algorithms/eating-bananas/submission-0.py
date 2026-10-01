import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=float('inf')
        arr=[]
        for i in range(1,max(piles)+1):
            arr.append(i)
        l,r=0,len(arr)-1
        while l<=r:
            hour=0
            m=(l+r)//2
            for i in piles:
                hour+=math.ceil(i/arr[m])
            if hour>h:
                l=m+1
            elif hour<=h:
                ans=min(ans,arr[m])
                r=m-1
        return ans

