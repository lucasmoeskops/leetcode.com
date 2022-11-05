# Score
#  Runtime: 65%
#  Memory usage: 80%

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_lookup = set(words)
        word_size = len(words[0])
        results = []
        
        for i in range(len(s) - word_size * len(words) + 1):
            j = i
            counter = None
            
            while True:
                word = s[j:j+word_size]
                
                if word in word_lookup:
                    if counter is None:
                        counter = Counter(words)
                        
                    occurrences_left = counter.get(word)
                    
                    if not occurrences_left:
                        break
                        
                    if occurrences_left == 1:
                        if sum(counter.values()) == 1:
                            results.append(i)
                            break
                        
                        del counter[word]
                    else:
                        counter[word] -= 1
                    
                    j += word_size
                else:
                    break
                    
        return results
