class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        count=0
        for i in range(len(speed)):
            while stack and (target-position[i])/speed[i] <=(target-position[stack[-1]])/speed[stack[-1]]:
                stack.pop()
                count+=1
            
            stack.append(i)
        return count