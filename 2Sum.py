''''Problem Description: https://leetcode.com/problems/two-sum/'''

# Solution using enumerate() and index()
def twoSum(nums, target):
	for i, v in enumerate(nums):
		if target - v in nums: # takes long time for large nums
      		j = nums.index(target - v)
      		if i == j: continue
      		else: return [i, j]
 
 
 # Solution using dictionary
 def twoSum(nums, target):
	dict = {}
	for i, v in enumerate(nums):
		if target - v in dict: return [i, dict[target - v]] # takes less time than searching in a list
		else: dict[v] = i 
'''
Don't need to store the indices of repeated values.
If the answer contains the indices of the same values, it will directly return at "if"
when encounters the second value.
'''  
