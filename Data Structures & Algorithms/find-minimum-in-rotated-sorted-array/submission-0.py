class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        for n in nums:
            if n < minimum:
                minimum = n

        return minimum
