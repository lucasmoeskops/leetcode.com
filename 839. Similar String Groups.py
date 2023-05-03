# Solution
#  Runtime: 67%
#  Memory usage: 93%
#
# Description
#
#  Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.
#
#  For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".
#
#  Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.
#
#  We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?
#

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        index = {s: i for i, s in enumerate(strs)}
        strs = list(index.keys())
        final_groups = set(index.values())

        equal_groups = defaultdict(list)
        groups = {}

        for i, s in enumerate(strs):
            for t in strs[i+1:]:
                swap = []
                match = True

                for k, (c, d) in enumerate(zip(s, t)):
                    if c != d:
                        if len(swap) == 2:
                            match = False
                            break

                        swap.append(k)

                if match and len(swap) == 2 and s[swap[0]] == t[swap[1]] and s[swap[1]] == t[swap[0]]:
                    equal_groups[index[s]].append(index[t])

        map_to = {}

        for a, bs in equal_groups.items():
            for b in bs:
                while a in map_to:
                    a = map_to[a]
                    
                while b in map_to:
                    b = map_to[b]
                
                if a == b:
                    continue

                map_to[max(a, b)] = min(a, b)
                final_groups.discard(max(a, b))

        return len(final_groups)
