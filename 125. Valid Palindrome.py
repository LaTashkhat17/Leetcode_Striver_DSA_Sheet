class Solution(object):
    def isPalindrome(self, s):
        str =  ""
        for i in s:
            if(i.isalnum()):
                str += i.lower()
        rev = str[::-1]
        if(str == rev): return True
        else: return False


obj1 = Solution()
ans = obj1.isPalindrome('A man, a plan, a canal: Panama')
ans = obj1.isPalindrome('W0000W')

print(ans)

