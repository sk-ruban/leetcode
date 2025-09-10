class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis = [] 

        for a in range(0,len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            
            l, r = a + 1, len(nums) - 1

            while l < r:
                total = nums[a] + nums[l] + nums[r]

                if total == 0:
                    lis.append([nums[a], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return lis