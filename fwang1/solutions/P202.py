class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        
        while n != 1:
            digit_char_list = []
            digit_char_list.extend(str(n))            
            unq_num = "".join(digit_char_list)
            
            if unq_num in visited:
                return False
            visited.add(unq_num)
            n = sum(map(lambda x: int(x) ** 2, digit_char_list))
        
        return True

if __name__  == "__main__":
    print Solution().isHappy(19)