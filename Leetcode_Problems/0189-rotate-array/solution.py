class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        print(nums[-k:])
        print(nums[:-k])
        nums[:] = nums[-k:] + nums[:-k]
