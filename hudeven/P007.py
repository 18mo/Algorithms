class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = (1 << 31) - 1
        MIN_INT = -MAX_INT - 1
        if x == MIN_INT: return 0

        res = 0
        p = x if x >= 0 else -x
        while p != 0:
            digit = p % 10
            if res <= MAX_INT // 10:
                res = res * 10 + digit
            else:
                return 0
            p = p // 10
        return res if x >= 0 else -res
