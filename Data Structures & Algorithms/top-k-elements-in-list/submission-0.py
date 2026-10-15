class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = freq.most_common()
        res = []
        for key, _ in ans:
            if k <= 0:
                break
            
            k -= 1
            res.append(key)
        
        return res
            

        