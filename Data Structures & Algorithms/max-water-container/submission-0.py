class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        volume = 0

        while l<r:
            vol = min(heights[l], heights[r]) * (r - l)
            volume = max(vol, volume)

            if heights[r]> heights[l]:
                l += 1
            
            else:
                r -= 1
        
        return volume



        