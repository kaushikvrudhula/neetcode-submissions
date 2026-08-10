class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i in range(0,len(temperatures)):
            if not stack:
                stack.append(i)
                continue
            if temperatures[stack[-1]]>=temperatures[i]:
                stack.append(i)
            while stack and (temperatures[stack[-1]]<temperatures[i]):
                result[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return result
            
            