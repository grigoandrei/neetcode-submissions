class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result_stack = []
        for num in tokens:
            if num == '+':
                 a = result_stack.pop()
                 b= result_stack.pop()
                 result_stack.append(a + b)
            elif num == '-':
                a = result_stack.pop()
                b = result_stack.pop()
                result_stack.append(b - a)
            elif num == '*':
                a = result_stack.pop()
                b = result_stack.pop()
                result_stack.append(a * b)
            elif num == '/':
                a = result_stack.pop()
                b = result_stack.pop()
                result_stack.append(int(float(b) / a))
            else:
                result_stack.append(int(num))
        return result_stack.pop()

    





        