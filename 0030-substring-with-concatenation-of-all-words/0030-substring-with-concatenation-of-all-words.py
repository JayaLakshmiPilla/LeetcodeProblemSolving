from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_count = Counter(words)
        
        result = []

        # Try each offset in word_len range
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1

                    # If there are too many of a word, shift the window
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len

                    # If all words matched
                    if right - left == total_len:
                        result.append(left)
                else:
                    # Reset counters if word not in list
                    current_count.clear()
                    left = right

        return result
