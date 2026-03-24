class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # 找到 left 和 right 的最高不同位，然后把 right 中该位及之后的所有位清零
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        
        return right << shift