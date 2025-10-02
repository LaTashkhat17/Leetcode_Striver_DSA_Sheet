class Solution(object):
    def func(self, nums):
        num_set = set(nums)
        ans = 0
        cnt = 0
        for i in num_set:
            if i - 1 not in num_set:
                cur_num = i
                cnt = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    cnt += 1
            ans = max(ans , cnt)
        
        return ans

# Read input from input.txt
with open('input.txt', 'r') as infile:
    # Read the numbers from the file and convert them into a list of integers
    nums = list(map(int, infile.read().split()))



# Create an instance of Solution
obj1 = Solution()

# Call the maxSubArray method with the input numbers
result = obj1.func(nums)

# Write the result to output.txt
with open('output.txt', 'w') as outfile:
    outfile.write(f"{result}\n")

