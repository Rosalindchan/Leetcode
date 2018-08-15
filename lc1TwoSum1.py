class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(nums[i])
                    result.append(nums[j])
                    return result
                    break



