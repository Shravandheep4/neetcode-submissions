from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        stack = deque()
        
        for character in s:

            if len(stack) != 0:
                top = stack[-1]
            else:
                top = ""


            if character in mapping and mapping[character] == top:
                stack.pop()
            else:
                stack.append(character)

        return True if len(stack) == 0 else False

            


        