class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for i in nums:
            d[i] = nums.count(i)

        result = any(v > 1 for v in d.values())       
        return result