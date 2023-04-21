# Solution
#  Runtime: 7%
#  Memory usage: 29%
#
# Description
#
#  You are given two strings, word1 and word2. You want to construct a string in the following manner:
#
#     Choose some non-empty subsequence subsequence1 from word1.
#     Choose some non-empty subsequence subsequence2 from word2.
#     Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
#
#  Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.
#
#  A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.
#
#  A palindrome is a string that reads the same forward as well as backward.
#


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        def test(i, j, k=False):
            if i == j:
                return 1
            
            if not k and (i >= len(word1) or j < len(s) - len(word2)):
                return 0
            
            if lookup[i][j][k] is None:
                if s[i] == s[j]:
                    lookup[i][j][k] = 2 + test(i+1, j-1, k=True) if j - i > 1 else 2
                else:
                    lookup[i][j][k] = max(test(i + 1, j, k=k), test(i, j - 1, k=k))
            
            return lookup[i][j][k]
            
        s = word1 + word2
        lookup = [[[None] * 2 for __ in range(len(s))] for _ in range(len(s))]
        t = test(0, len(s)-1)
        return t if t > 1 else 0
