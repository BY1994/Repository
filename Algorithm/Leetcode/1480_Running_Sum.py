class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        returns = [0]*len(nums);
        returns[0] = nums[0];
        for i in range(1, len(nums)):
            returns[i] += returns[i-1] + nums[i];
        return returns
