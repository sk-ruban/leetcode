class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        count = 0
        maxHeap = [-n for n in nums]
        heapq.heapify(maxHeap)

        while k:
            n = heapq.heappop(maxHeap)
            count += n
            k -= 1
            heapq.heappush(maxHeap, floor(n / 3))

        return -count