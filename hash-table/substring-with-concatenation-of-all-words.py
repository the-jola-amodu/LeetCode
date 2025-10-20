from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []

        if not words:
            return output

        words_count = defaultdict(int)
        word_len = len(words[0])
        num_of_words = len(words)

        for word in words:
            words_count[word] += 1

        for i in range(word_len):
            left = i
            window = defaultdict(int)
            words_found = 0

            for right in range(i, len(s) - (word_len - 1), word_len):
                current_word = s[right:right + word_len]
                if current_word in words:
                    words_found += 1
                    window[current_word] += 1

                    while window[current_word] > words_count[current_word]:
                        word_to_remove = s[left:left + word_len]
                        window[word_to_remove] -= 1
                        words_found -= 1
                        left += word_len

                    if words_found == num_of_words:
                        output.append(left)
                        word_to_remove = s[left:left + word_len]
                        window[word_to_remove] -= 1
                        words_found -= 1
                        left += word_len
                else:
                    window.clear()
                    words_found = 0
                    left = right + word_len
        return output
