class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate, count = None, 0

        for x in nums:
            if count == 0:
                candidate = x
                count = 1
            elif x == candidate:
                count += 1
            else:
                count -= 1

        return candidate
    
    def majorityElement2(self, nums: List[int]) -> int:
        map = {}
        length = len(nums) // 2

        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map[num] > length:
                return num
            
    def majorityElement3(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2] 