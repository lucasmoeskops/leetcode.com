# Score
#  Runtime: 88%
#  Memory usage: 36%
#
# Description
#
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
#
#    Every adjacent pair of words differs by a single letter.
#    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
#    sk == endWord
#
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].
#

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        try:
            start_index = wordList.index(beginWord)
        except ValueError:
            start_index = len(wordList)
            wordList.append(beginWord)

        end_index = wordList.index(endWord)
        word_hashes = []
        hash_to_words = defaultdict(list)

        for i, word in enumerate(wordList):
            for_word = []

            for skip in range(len(word)):
                hashed_word = word[:skip] + "_" + word[skip+1:]
                hash_to_words[hashed_word].append(i)
                for_word.append(hashed_word)

            word_hashes.append(for_word)

        graph = [set() for i in range(len(wordList))]

        for hash, word_indices in hash_to_words.items():
            for i in word_indices:
                for j in word_indices:
                    if i != j:
                        graph[i].add(j)
                        graph[j].add(i)

        distances = [inf] * len(wordList)
        distances[start_index] = 0
        queue = deque([start_index])
        
        while queue:
            index = queue.popleft()

            if index == end_index:
                break

            distance = distances[index] + 1

            for node in graph[index]:
                if distances[node] > distance:
                    distances[node] = distance
                    queue.append(node)
        
        if distances[end_index] == inf:
            return []
        
        queue = [[end_index]]
        routes = []
        
        while queue:
            route = queue.pop()
            distance = distances[route[0]] - 1
            
            if distance < 0:
                routes.append([wordList[i] for i in route])
                continue
            
            for node in graph[route[0]]:
                if distances[node] == distance:
                    queue.append([node] + route)
        
        return routes
