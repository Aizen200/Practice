class Solution:
    def isValid(self, s: str) -> bool:
        var=0
        arr=[]
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                arr.append(s[i])
                var+=1
            elif arr and arr[-1]=="(" and s[i]==")":
                arr.pop()
                var-=1
            elif arr and arr[-1]=="{" and s[i]=="}":
                arr.pop()
                var-=1
            elif arr and arr[-1]=="[" and s[i]=="]":
                arr.pop()
                var-=1
        if var!=0:
            return False
        return True