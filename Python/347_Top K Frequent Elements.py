from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        for num, cnt in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (cnt, num))
            else:
                if cnt > heap[0][0]:
                    heapq.heapreplace(heap, (cnt, num))
        return [num for _, num in heap]