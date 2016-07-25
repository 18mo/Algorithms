class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(1, rowIndex + 1):
        	res.append(res[-1] * (rowIndex - i + 1) / i)
        return res



if __name__ == "__main__":
	print Solution().getRow(4)
