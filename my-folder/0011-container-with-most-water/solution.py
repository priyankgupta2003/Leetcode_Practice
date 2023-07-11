class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1

        while left < right:
            width = right - left
            area = max (area, min(height[left],height[right])*width)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1
        return area


