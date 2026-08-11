class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        p_counter = Counter(p)
        for right in range(len(s)-len(p)+1):
            curr_string = s[right:right+len(p)]
            if Counter(curr_string) == p_counter:
                result.append(right)
        return result