import math
class Solution(object):
    def isPerfectSquare(self, num):
        start = int(math.pow(2, math.floor(math.log(num, 2)/ 2)))
        end =  start * 2
        
        while start <= end:
            mid = (start + end) / 2
            sqr = mid * mid 
            if sqr > num:
                end = mid - 1
            elif sqr < num:
                start = mid + 1
            else: 
                return True 
        return False