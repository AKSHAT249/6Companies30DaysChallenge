class Solution:  
    def evalRPN(self, tokens: List[str]) -> int:

        operator = ["+" , "-", "*" , "/"]

        def solve(value1, value2 , symbol):
            if symbol=="+":
                return value1+value2
            elif symbol=="*":
                return value1*value2
            elif symbol=="/":
                return int(value2/value1)
            elif symbol=="-":
                return value2-value1
        
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
            else:
                value1 = stack.pop()
                value2 = stack.pop()
                symbol = tokens[i]
                value = solve(value1, value2, symbol)
                stack.append(value)
        return stack.pop()
