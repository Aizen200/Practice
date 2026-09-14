class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums=set(nums)
        nums=list(nums)
        nums.sort()
        count=1
        obj={}
        for i in nums:
            if i-1 in obj:
                count+=obj[i-1]
            obj[i]=1
        print(obj)
        return count
