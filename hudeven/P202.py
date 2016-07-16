class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        sumSet = set()
        cur = n
        while True:
            sum = 0
            while cur:
                digit = cur % 10
                cur = cur // 10
                sum += digit * digit
            if sum == 1:
                return True
            elif sum in sumSet:
                return False
            else:
                sumSet.add(sum)
                cur = sum

def test():
    print Solution().isHappy(1)
    print Solution().isHappy(2)
    print Solution().isHappy(3)
    print Solution().isHappy(4)
    print Solution().isHappy(998)

if __name__ == "__main__":
    test()
