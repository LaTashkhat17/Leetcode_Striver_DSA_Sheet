
class Solution(object):
    def maxProfit(self, nums):
        s = len(nums)
        minp = [0] * s
        maxp = [0] * s
        minp[0] = nums[0]
        maxp[-1] = nums[-1]
        maxprofit = 0
       
        for i in range(1, s):
            minp[i] = min(nums[i], minp[i - 1])
            maxp[s - i - 1] = max(nums[s - i - 1], maxp[s - i])
        #return minp, maxp
        
        for i in range(1, s):
            maxprofit = max((maxp[i] -minp[i - 1]), maxprofit)
        return maxprofit
    def maxProfitalt(self, nums):
        maxp = 0
        minp = 100000000
        for i in range(len(nums)):
            if(nums[i] < minp):
                minp = nums[i]
            else:
                if((nums[i] - minp) > maxp):
                    maxp = nums[i] - minp
        return maxp
with open('input.txt', 'r') as infile:
    # Read the numbers from the file and convert them into a list of integers
    nums = list(map(int, infile.read().split()))

# Create an instance of Solution
obj1 = Solution()

# Call the maxSubArray method with the input numbers
result = obj1.maxProfit(nums)

# Write the result to output.txt
with open('output.txt', 'w') as outfile:
    outfile.write(f"{result}\n")
