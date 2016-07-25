class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        occured = set()
        res = []
        for i in range(len(s) - 9):
        	sq = s[i : i + 10]
        	if sq in occured: 
        		res.append(sq)
        	else:
        		occured.add(sq)
        return list(set(res))


if __name__  == "__main__":
	s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
	s1= "AAAAAAAAAAA"
	print Solution().findRepeatedDnaSequences(s1)