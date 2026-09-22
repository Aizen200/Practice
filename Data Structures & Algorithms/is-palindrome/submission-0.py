class Solution:
    def isPalindrome(self, s: str) -> bool:
        ab1=""
        for i in s:
            if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57:
                ab1+=i.lower()
        l=0
        r=len(ab1)-1
        while l<=r:
            if ab1[l]!=ab1[r]:
                return False
            l+=1
            r-=1
        return True