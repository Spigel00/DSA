class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    
        seen = {}  # number -> index

        for index, value in enumerate(nums):
            needed = target - value

            if needed in seen:
                return [seen[needed], index]

            seen[value] = index
