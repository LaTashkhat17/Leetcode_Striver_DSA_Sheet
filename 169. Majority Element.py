class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        #return nums
        maxi = 0
        cnt = 1
        maxv = -1
        k = 1
        for i in range(1, len(nums)):
            if(nums[i] == nums[i - 1]):
                cnt += 1
            else:
                if(maxi < cnt):
                    maxv = nums[i - 1]
                    maxi = max(maxi, cnt)
                    cnt = 1
            k = i
        #return k
        if(maxi < cnt):
            maxv = nums[k - 1]
            maxi = max(maxi, cnt)
        return maxv, maxi
    
    def majorityElementalt(self, nums):
        nums.sort()
        return(nums[len(nums)//2])

        

obj1 = Solution()
print(obj1.majorityElement([2,2,1,1,1,2,2]))
print(obj1.majorityElement([1]))