class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, val in enumerate(nums):
            if val not in seen:
                seen[val] = i
            else:
                if i - seen[val] <= k:
                    return True
                else:
                    seen[val] = i

        return False