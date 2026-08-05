class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        total_length = 0
        for word in words:
            word_count = Counter(word)
            if word_count <= chars_count:
                total_length+=len(word)
        return total_length
            