class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numss = {nums[i]:i for i in range(len(nums))}
        for i in range(len(nums)-1):
            cha = target - nums[i]
            if cha in numss and i != numss[cha]:
                return [i, numss[cha]]