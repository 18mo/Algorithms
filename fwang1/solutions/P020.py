class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return False

        dict = {
            ')':'(',
            ']':'[',
            '}':'{'
            }
            
        stack = []
        
        for i in range(len(s)):
            if s[i] in dict.values():
                stack.append(s[i])
            if s[i] in dict.keys():
                if not stack:
                    return False
                if stack.pop() != dict[s[i]]:
                    return False
        
        return len(stack) == 0
