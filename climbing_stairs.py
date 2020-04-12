# Brute Force: Time exceeded

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.cs(0,n)
    
    def cs(self,i,n):
        if i>n:
            return 0
        if i == n:
            return 1
        return self.cs(i+1,n) + self.cs (i+2,n)

# Dynamic programming subproblem
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        table = {}
        table[1] = 1
        table[2] = 2
        i = 3
        while i <= n:
            table[i] = table[i-1] + table[i-2]
            i+=1
        return table[n]

# Check Binet's method