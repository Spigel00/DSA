class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        equal = []
        higher = []
        for i in range(len(nums)):
            if nums[i]<pivot:
                smaller.append(nums[i])
            elif nums[i]>pivot:
                higher.append(nums[i])
            elif nums[i]==pivot:
                equal.append(nums[i])
        ans = smaller+equal+higher
        return ans