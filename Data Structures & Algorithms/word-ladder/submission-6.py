class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        # bidirectional BFS
        begin_set = {beginWord}
        end_set = {endWord}

        step = 1
        word_len = len(beginWord)

        while begin_set and end_set:
            # key optimization, always start from the set with fewer elements
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
            
            next_set = set()

            for word in begin_set:
                word_chars = list(word)
                for i in range(word_len):
                    original_char = word_chars[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == original_char:
                            continue
                        word_chars[i] = c
                        target = "".join(word_chars)

                        if target in end_set:
                            return step + 1
                        if target in word_set:
                            next_set.add(target)
                            word_set.remove(target)
                    word_chars[i] = original_char
            begin_set = next_set
            step += 1
        return 0
