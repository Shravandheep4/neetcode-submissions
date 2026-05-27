class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        

        stack = []

        for i in s:

            if i in ['(', '[', '{']:
                stack.append(i)

            else:
                bracket = mapping.get(i)
                
                if stack and stack[-1] == bracket:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False
