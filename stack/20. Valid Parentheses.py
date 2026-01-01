class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2: 
            return False 

        stack = [] 
        opening = "({["
        amtClosing = 0 
        
        for bracket in s: 
            if bracket in opening: 
                stack.append(bracket)
            else: 
                amtClosing += 1 
                if len(stack) == 0: 
                    return False 
                openBracket = stack.pop()
                if bracket == ")": 
                    if openBracket != "(":
                        return False 
                elif bracket == "}": 
                    if openBracket != "{": 
                        return False 
                else: 
                    if openBracket != "[": 
                        return False
        if amtClosing != (len(s) / 2): 
            return False 
        return True 