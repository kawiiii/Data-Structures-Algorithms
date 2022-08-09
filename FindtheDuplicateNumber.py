"""
 Initially I used = > return [i for i in nums if nums.count(i) >=2][0] to solve the problem but its time complexity was heavily dependant on the size of array so 
 I faced the Time exceeded error. Then I optimized to use the two pointer approach as it forms cyclic linked list and used floyd warshal to get the element that repeats
 Time Complexity = O (N) and Space Complexity = O (1) 
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow , fast = 0 , 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast=0
        while True:
            slow = nums[slow]
            fast= nums[fast]
            if slow == fast:
                return slow
