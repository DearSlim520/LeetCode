import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = [0] * (len(w) + 1)
        for i in range(1, len(w) + 1):
            self.prefixSum[i] = self.prefixSum[i-1] + w[i-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefixSum[-1])
        left, right = 1, len(self.prefixSum) - 1
        while left < right:
            mid = left + (right - left) // 2
            if self.prefixSum[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()