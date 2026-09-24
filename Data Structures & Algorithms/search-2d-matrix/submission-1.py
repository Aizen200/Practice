class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            l=0
            r=len(i)-1
            while l<=r:
                m=(l+r)//2
                if i[m]==target:
                    return True
                elif i[m]<target:
                    l=m+1
                elif i[m]>target:
                    r=m-1
        return False