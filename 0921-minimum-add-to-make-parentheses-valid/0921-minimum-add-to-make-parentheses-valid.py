class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] in ")}]":
                if stack and stack[-1]=="(" and s[i]==")":
                    stack.pop() 
                elif stack and stack[-1]=="[" and s[i]=="]":
                    stack.pop() 
                elif stack and stack[-1]=="{" and s[i]=="}":
                    stack.pop() 
                else:
                    stack.append(s[i])
                
        
        return len(stack)
        
        