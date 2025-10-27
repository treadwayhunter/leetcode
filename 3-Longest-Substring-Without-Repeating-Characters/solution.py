class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window = {}
        best = 0
        #right = 0
        left = 0

        # sliding window, but ensure the left can move too

        for i, ch in enumerate(s):
            #right = i # current index
            if ch in window:
                new_pos = window[ch] + 1
                if left <= new_pos:
                    left = new_pos # one to the right of last seen value
                        
            window[ch] = i
            new_score = i + 1 - left
            if new_score > best:
                best = new_score
 
        return best