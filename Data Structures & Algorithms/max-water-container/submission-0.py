class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans= float('-infinity')
        l=0
        r=len(heights)-1
        while l<r:
            area= (r-l)*min(heights[l],heights[r])
            if heights[l]<heights[r]:
                l+=1
            elif heights[l]>heights[r]:
                r-=1
            elif heights[l]==heights[r]:
                l+=1
            ans=max(ans,area)
        return ans