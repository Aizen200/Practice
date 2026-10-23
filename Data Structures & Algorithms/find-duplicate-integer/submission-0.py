class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        obj={}
        for i in nums:
            obj[i]=1+obj.get(i,0)
        for i in obj:
            if obj[i]>1:
                return i
        