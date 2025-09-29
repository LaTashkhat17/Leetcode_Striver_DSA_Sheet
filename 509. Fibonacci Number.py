class Solution(object):
    def fib(self, n):
        if(n == 0): return 0
        if(n == 1): return 1
        f = [0, 1]
        for i in range(2, n + 1):
            f.append(f[i - 1] + f[i - 2])
        return f[i]
    
obj1 = Solution()
print(obj1.fib(5))
        