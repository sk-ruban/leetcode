# Not optimal as we can preprocess it to make range sum queries more efficient
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums 

    def sumRange(self, left: int, right: int) -> int:
        sum = 0
        for i in range(left, right + 1):
            sum += self.nums[i]
        return sum

# Optimal
class NumArray2:
    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]