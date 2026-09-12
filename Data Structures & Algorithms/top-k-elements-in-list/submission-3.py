class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj={}
        for i in nums:
            obj[i]=1+obj.get(i,0)
        arr=sorted(obj.items(),key=lambda item: item[1],reverse=True)
        arr2=[]
        for i in arr:
            arr2.append(list(i))
        ans=[]
        for i in range(k):
            ans.append(arr2[i][0])
        return ans