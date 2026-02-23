class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [:k][k+1:] = [n-k-1:][:n-k]
        if k == 0:
            return nums

        # 补位
        n = len(nums)
        tmp = nums[n-k-1:]
        k = k % n
        p = n-k-1
        i = n - 1
        while p >= 0:
            nums[i] = nums[p]
            p -= 1
            i -= 1
        
        for t in range(len(tmp)-1, -1, -1):
            nums[i] = tmp[t]
            i -= 1

        return nums