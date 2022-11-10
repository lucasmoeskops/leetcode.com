# Score:
#   Runtime: 41%
#   Memory usage: 60%

def findPaths(board, word, sx, sy):
    """ Find paths for given word on the board starting from (sx, sy) """
    m = len(board[0])
    n = len(board)
    
    queue = deque([(sx, sy, len(word), [])])
    
    paths = []
    
    while queue:
        x, y, l, p = queue.popleft()

        if l == 1:
            paths.append(p + [(x, y)])
            continue
            
        r = p + [(x, y)]
        l -= 1
        c = word[len(word) - l]

        if x > 0 and board[y][x-1] == c and (x-1, y) not in p:
            queue.append((x-1, y, l, r))
        if y > 0 and board[y-1][x] == c and (x, y-1) not in p:
            queue.append((x, y-1, l, r))
        if x < m - 1 and board[y][x+1] == c and (x+1, y) not in p:
            queue.append((x+1, y, l, r))
        if y < n - 1 and board[y+1][x] == c and (x, y+1) not in p:
            queue.append((x, y+1, l, r))
            
    return paths


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board[0])
        n = len(board)
        results = []
        
        occurrences = defaultdict(list)
        for y, row in enumerate(board):
            for x, val in enumerate(row):
                occurrences[val].append((x, y))
        
        for word in words:
            # We need to check the least paths if we start at the letter that occurs least frequently in the board
            rarest_letter = (None, m*n+1)
            for letter in word:
                o = len(occurrences[letter])
                if o < rarest_letter[1]:
                    rarest_letter = (letter, o)
                    if o < 2:
                        break
            
            if rarest_letter[1] == 0:
                continue
            
            rl = rarest_letter[0]
            ri = word.index(rl)
            before = word[:ri] + rl
            after = word[ri:]

            for x, y in occurrences[rl]:
                # See if there is a combination for before path and after path
                # that doesn't overlap to confirm that the word is findable
                if len(before) > 1:
                    before_paths = findPaths(board, before[::-1], x, y)
                else:
                    if findPaths(board, after, x, y):
                        results.append(word)
                        break
                    continue
                    
                after_paths = [set(p) for p in findPaths(board, after, x, y)]

                for path in before_paths:
                    as_set = set(path[1:])
                    for path2 in after_paths:
                        if not (path2 & as_set):
                            results.append(word)
                            break
                    else:
                        continue
                    break
                else:
                    continue
                
                break
        
        return results
     
