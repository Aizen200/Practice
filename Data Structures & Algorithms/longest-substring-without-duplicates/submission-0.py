class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        add=set()
        l=0
        ans=0
        for r in range (len(s)):
            while s[r] in add:
                add.remove(s[l])
                l+=1
            add.add(s[r])
            ans=max(ans,len(add))
        return ans
        