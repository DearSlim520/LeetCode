class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # 把 n 的最低位取出，放到 result 的最高位
            result = (result << 1) | (n & 1)
            n >>= 1                    # n 右移一位
        return result