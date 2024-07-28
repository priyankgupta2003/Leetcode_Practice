class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while low < high:
            sm = numbers[low] + numbers[high]
            if sm == target:
                return [low + 1, high + 1]
            elif sm < target:
                low = low + 1
            else:
                high = high - 1

        return [-1, -1]

