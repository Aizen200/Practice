class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        obj={}
        for i in nums:
            obj[i]=1+obj.get(i,0)
        for i in obj:
            if obj[i]>len(nums)/2:
                return i
                
        