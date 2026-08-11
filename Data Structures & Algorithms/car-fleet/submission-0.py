class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed =[]
        stack=[]
        for index in range(0,len(speed)):
            pos_speed.append([position[index],speed[index]])
        pos_speed.sort(key=lambda x:x[0],reverse=True)
        for index in range(0,len(pos_speed)):
            timeTaken=(pos_speed[index][0]-target)/pos_speed[index][1]
            if not stack:
                stack.append(timeTaken)
                continue
            if stack[-1] > timeTaken:
                stack.append(timeTaken)
            else:
                continue
        return len(stack)