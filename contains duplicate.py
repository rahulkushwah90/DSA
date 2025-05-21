"""
Contains Duplicate
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false
"""

# Approach: Hash Set
# The idea is to use a hash set to keep track of the elements we have seen so far.
# If we encounter an element that is already in the hash set, we return True.
# If we finish iterating through the list without finding any duplicates, we return False.


from typing import List
nums = [1, 2, 3, 4, 5, 1]  # Example input list
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
solution = Solution()
result = solution.containsDuplicate(nums)
print(result) 

# Time complexity: O(n) 
# Space complexity: O(n)
# where n is the length of the input list nums  
# The time complexity is O(n) because we are iterating through the list once, and the space complexity is O(n) because we are using a hash set to store the elements.