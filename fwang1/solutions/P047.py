class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		return list(map(list, self.get_permute(nums)))
  
	def get_permute(self, nums):
		if nums:
			prev = self.get_permute(nums[:-1])
			cur = nums[-1]
			return self.add_num(prev, cur)
		else:
			return set()        
		
	def add_num(self, ll, num):
		res = set()
		if not ll: return [(num,)]
		for l in ll:
			for i in range(len(l) + 1):
				res.add(l[:i] + (num,) + l[i:])
		return res

if __name__ == "__main__":
    print Solution().permuteUnique([2,2,1,1])