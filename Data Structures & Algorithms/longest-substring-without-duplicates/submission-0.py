class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        charSet = set()
        l = 0
        n = len(s)

        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            w = (r -l)+ 1
            count = max(count, w)
            charSet.add(s[r])

        return count

            
        