class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum=0
        nums.sort()
        for i in range(0,len(nums)-1,2):
            sum+=nums[i]
        return sum