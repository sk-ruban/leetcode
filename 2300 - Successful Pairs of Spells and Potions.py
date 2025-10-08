class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        numPotions = len(potions)

        for s in spells:
            l, r = 0, numPotions - 1
            idx = numPotions

            if potions[numPotions - 1] * s < success:
                res.append(0)
                continue

            while l <= r:
                m = (l + r) // 2
                if s * potions[m] >= success:
                    r = m - 1
                    idx = m
                else:
                    l = m + 1

            res.append(numPotions - idx)

        return res
