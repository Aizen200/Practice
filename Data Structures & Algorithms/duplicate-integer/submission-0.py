class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj={}
        for i in nums:
            obj[i]=1+obj.get(i,0)
        for i in obj:
            if obj[i]>1:
                return True
        return False