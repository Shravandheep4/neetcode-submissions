import ast

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        numeric_response = None

        for token in tokens:

            # Do the math
            if token in ['+', '-', '*', '/']:
                value1 = stack.pop()
                value2 = stack.pop()
                mathematical_expression = str(value2) + token + str(value1)
                numeric_response = int(eval(mathematical_expression))
                
                stack.append(numeric_response)

            else:
                number = int(token)
                stack.append(number)

        return numeric_response if numeric_response else stack[-1]
                
        