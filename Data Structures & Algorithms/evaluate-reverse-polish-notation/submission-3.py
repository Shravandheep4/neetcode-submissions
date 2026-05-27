import math
from collections import deque

class Solution:

    @staticmethod
    def evaluate_expression(op1, op2, operator):

        print(op1, operator, op2)

        op1 = int(op1)
        op2 = int(op2)

        if operator == '+':
            return op1 + op2
        if operator == '-':
            return op1 - op2
        if operator == '/':
            return op1 / op2
        if operator == '*':
            return op1 * op2


    def evalRPN(self, tokens: List[str]) -> int:

        stack = deque()

        for token in tokens:

            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                token = int(token)
                stack.append(token)

            elif not token.isdigit():
                operator = token
                operand_2 = stack.pop()
                operand_1 = stack.pop()

                value = self.evaluate_expression(operand_1, operand_2, operator)
                stack.append(value)

        return int(stack.pop())



        