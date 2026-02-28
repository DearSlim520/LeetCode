import random
from typing import List

class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.nums.append(val)
        self.val_to_idx[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        
        target_idx = self.val_to_idx[val]
        self.val_to_idx[self.nums[-1]] = target_idx
        # swap with last element
        self.nums[-1], self.nums[target_idx] = self.nums[target_idx], self.nums[-1]
        self.nums.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()