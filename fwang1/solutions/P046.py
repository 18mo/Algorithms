class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if nums:
            prev = self.permute(nums[:-1])
            cur = nums[-1]
            res.extend(self.add_num(prev, cur))        
        return res
        
    def add_num(self, ll, num):
        res = []
        if not ll: return [[num]]
        for l in ll:
           for i in range(len(l) + 1):
               res.append(l[:i] + [num] + l[i:])
        return res

if __name__ == "__main__":
    print Solution().permute([1,2,3])