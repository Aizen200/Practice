class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset=set(nums)
        ans=0
        for i in numsset:
            if i-1 not in numsset:
                length=0
                while i+length in numsset:
                    length+=1
                ans=max(ans,length)
        return ans