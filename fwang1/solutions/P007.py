class Solution(object):
    # convert to string and swap the head and tail
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        MAX_INT = 1 << 31

        sign = ""
        intstr = []
        intstr.extend(str(x))
        if intstr[0] == '-':
            sign = "-"
            intstr = intstr[1:]

        x_len = len(intstr)
        if x_len > len(str(MAX_INT)): return 0

        # swap the head and tail
        for i in range(x_len / 2):
            tmp = intstr[i]
            intstr[i] = intstr[-i-1]
            intstr[-(i + 1)] = tmp

        res = "".join(intstr)
        if x_len == len(str(MAX_INT)):
            if sign:
                if res > str(MAX_INT):
                    return 0
            else:
                if res > str(MAX_INT - 1):
                    return 0

        return  int(sign + res)

    def reverse(self, x):
        MAX_INT = (1 << 31) - 1
        
        if x ==  - MAX_INT - 1: return 0
        
        neg_flag = -1 if x < 0 else 1
        x = -x if x < 0 else x

        res = 0
        while x:
            if res > MAX_INT/ (10): return 0
            digit = x % 10
            if res * 10 > MAX_INT - digit:
                return 0
            elif res * 10  > MAX_INT - digit - 1 and neg_flag > 0:
                return 0
            res = res * 10 + x % 10
            x /= 10

        return res * neg_flag

def test1():    
    print Solution().reverse(12345) == 54321
    print Solution().reverse(10003) == 30001
    print Solution().reverse(-1000) == -1
    print Solution().reverse(-2001) == -1002
    print Solution().reverse(-100000000000) == -1
    print Solution().reverse(-2147483412) == -2143847412

if __name__ == "__main__":	
    test1()


    
