class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)  # Correct usage of `len` as a function
        for i in range(n):
            for j in range(i + 1, n):  # Compare elements after the current index
                if nums[i] == nums[j]:
                    return True  # Correct capitalization of `True`
        return False  # Correct capitalization of `False`