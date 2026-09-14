class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj={}
        ans=[]
        for i in nums:
            obj[i]=1+obj.get(i,0)
        for i in obj:
            if obj[i]>=k:
                ans.append(i)
        return ans