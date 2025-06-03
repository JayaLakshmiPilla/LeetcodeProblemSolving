from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            # Determine how many words fit into the current line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            line_words = words[i:j]
            num_words = j - i
            is_last_line = (j == n)

            if num_words == 1 or is_last_line:
                # Left-justified
                line = ' '.join(line_words)
                line += ' ' * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                spaces_between_words = num_words - 1
                even_space = total_spaces // spaces_between_words
                extra_space = total_spaces % spaces_between_words

                line = ''
                for k in range(spaces_between_words):
                    line += line_words[k]
                    line += ' ' * (even_space + (1 if k < extra_space else 0))
                line += line_words[-1]

            res.append(line)
            i = j

        return res
