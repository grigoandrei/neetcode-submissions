class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []
        for i in count.keys():
            heapq.heappush(heap, (count[i], i))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for num in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
            
            
        