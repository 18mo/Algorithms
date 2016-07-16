class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if dict.get(c):
                stack.append(c)
            else:
                if stack:
                    if c != dict[stack.pop()]:
                        return False
                else:
                    return False
        return len(stack) == 0
