# Score:
#  Runtime: 97%
#  Memory usage: 38%
#
# Description:
#   A transformation sequence from word beginWord to word endWord using a dictionary wordList is 
#   a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
#   * Every adjacent pair of words differs by a single letter.
#   * Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#   * sk == endWord
#
#   Given two words, beginWord and endWord, and a dictionary wordList, return the number of words
#   in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
#

from collections import defaultdict, deque


def make_word_map(words):
    map_ = defaultdict(list)
    for word in words:
        for split_at in range(len(word)):
            map_[word[:split_at] + " " + word[split_at+1:]].append(word)
    return map_


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = {beginWord}
        queue = deque([(beginWord, 1)])
        word_map = make_word_map([beginWord, *wordList])
        while queue:
            word, distance = queue.popleft()
            num_transformations = distance + 1
            for split_at in range(len(word)):
                for other_word in word_map[word[:split_at]+" "+word[split_at+1:]]:
                    if other_word not in seen:
                        seen.add(other_word)
                        if other_word == endWord:
                            return num_transformations
                        queue.append((other_word, num_transformations))
        return 0
