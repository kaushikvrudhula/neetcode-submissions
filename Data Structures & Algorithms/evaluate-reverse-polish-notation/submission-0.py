class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        value=[]
        result=0
        for token in tokens:
            if token=='-':
                a,b=value.pop(),value.pop()
                value.append(b-a)
            elif token=='+':
                a,b=value.pop(),value.pop()
                value.append(a+b)
            elif token=='*':
                value.append(value.pop()*value.pop())
            elif token=='/':
                a,b=value.pop(),value.pop()
                value.append(int(float(b)/a))
            else:
                value.append(int(token))
        return value[0]