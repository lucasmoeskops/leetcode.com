# Score:
#   Runtime: 49%
#   Memory usage: 13%
#
# Comment: lots to learn about goniometry and 2d algorithms
#
# Description:

def get_slope(x1, y1, x2, y2):
    """ Get integer x and y increments towards x2, y2 """
    dx, dy = x2-x1, y2-y1
    f = gcd(dx, dy)
    return (dx//f, dy//f) if f else (dx, dy)
    

class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        # Sort items clockwise and assumes they are on boundaries
        def sort_key(tree):
            x, y = tree
            if x == xMin:
                return 3, -y
            elif x == xMax:
                return 1, y
            elif y == yMin:
                return 0, x
            elif y == yMax:
                return 2, -x
            elif x <= topLeft and y >= leftTop:
                return 2, -x
            elif x <= bottomLeft and y < leftBottom:
                return 3, -y
            elif x >= bottomRight and y <= rightBottom:
                return 0, x
            elif x >= topRight and y >= rightTop:
                return 1, y
            
        # Solve the simple cases
        if len(trees) <= 1:
            return trees
        
        # Find the rectangular boundaries
        x, y = trees[0]
        xMin, xMax, yMin, yMax = x, x, y, y
        topLeft, topRight, rightTop, rightBottom, bottomRight, bottomLeft, leftBottom, leftTop = x, x, y, y, x, x, y, y
        for x, y in trees:
            if x <= xMin:
                xMin = x
            if x >= xMax:
                xMax = x
            if y <= yMin:
                yMin = y
            if y >= yMax:
                yMax = y
                
        # Find up to 8 points that define the outer octogonal bounds
        topLeft, topRight, rightTop, rightBottom, bottomRight, bottomLeft, leftBottom, leftTop = xMax, xMin, yMin, yMax, xMin, xMax, yMax, yMin
        for x, y in trees:
            if x == xMin:
                leftTop = max(leftTop, y)
                leftBottom = min(leftBottom, y)
            if x == xMax:
                rightTop = max(rightTop, y)
                rightBottom = min(rightBottom, y)
            if y == yMin:
                bottomLeft = min(bottomLeft, x)
                bottomRight = max(bottomRight, x)
            if y == yMax:
                topLeft = min(topLeft, x)
                topRight = max(topRight, x)
        
        # Find items that are on the rectangular borders
        on_borders = []
        for x, y in trees:
            if x == xMin or x == xMax or y == yMin or y == yMax:
                on_borders.append((x, y))
        
        ordered = sorted(on_borders, key=sort_key)
        
        pivotal = []
        
        lines = []
        for i, (x, y) in enumerate(ordered):
            x2, y2 = ordered[(i + 1) % len(ordered)]
            dx, dy = get_slope(x, y, x2, y2)
            lines.append((dx, dy))
            # Here could come some optimisations to ignore some items but not yet succesful
            pivotal.append(((x, y), (dx, dy)))
        
        ordered = set(ordered)
        
        # We add elements that are outside of the simple bounds and might be required in the final list
        extra_candidates = defaultdict(list)
        
        for x, y in trees:
            if (x, y) in ordered:
                continue
            for i, ((sx, sy), (dx, dy)) in enumerate(pivotal):
                if dx > 0 and dy > 0 and (x - sx) * dy / dx >= (y - sy):
                    extra_candidates[i].append((x, y))
                elif dy > 0 and dx < 0 and (x - sx) * dy / dx <= (y - sy):
                    extra_candidates[i].append((x, y))
                elif dx < 0 and dy < 0 and (x - sx) * dy / dx <= (y - sy):
                    extra_candidates[i].append((x, y))
                elif dx > 0 and dy < 0 and (x - sx) * dy / dx >= (y - sy):
                    extra_candidates[i].append((x, y))
                else:
                    continue
                    
                break
                 
        # We try to find candidates that are covered by other candidates and ignore them for our final list.
        ignore = set()
        for i, trees_ in extra_candidates.items():
            (x1, y1), (sdx, sdy) = pivotal[i]
            (x2, y2), _ = pivotal[(i + 1) % len(pivotal)]
            for j, (sx, sy) in enumerate(trees_):
                slopes = get_slope(x1, y1, sx, sy), get_slope(sx, sy, x2, y2)
                for k, (x4, y4) in enumerate(trees_):
                    if j == k:
                        continue
                        
                    if sdx > 0 and sdy > 0:
                        dx, dy = slopes[x4 < sx]
                    elif sdx < 0 and sdy > 0:
                        dx, dy = slopes[y4 < sy]
                    elif sdx < 0 and sdy < 0:
                        dx, dy = slopes[x4 > sx]
                    else:
                        dx, dy = slopes[y4 > sy]
                        
                    if dx > 0 and dy > 0 and (x4 - sx) * dy / dx > (y4 - sy):
                        ignore.add((sx, sy))
                    elif dy > 0 and dx < 0 and (x4 - sx) * dy / dx < (y4 - sy):
                        ignore.add((sx, sy))
                    elif dx < 0 and dy < 0 and (x4 - sx) * dy / dx < (y4 - sy):
                        ignore.add((sx, sy))
                    elif dx > 0 and dy < 0 and (x4 - sx) * dy / dx > (y4 - sy):
                        ignore.add((sx, sy))
                    else:
                        continue
                        
                    break
                    
        for trees_ in extra_candidates.values():
            for tree in trees_:
                if tree not in ignore and tree not in ordered:
                    ordered.add(tree)
                    
        # Recalculate order and slopes
        ordered = sorted(ordered, key=sort_key)
        
        lines = []
        for i, (x, y) in enumerate(ordered):
            x2, y2 = ordered[(i + 1) % len(ordered)]
            lines.append(get_slope(x, y, x2, y2))
        
        # Detect elements that bound too much inwards and remove them since they are redundant
        to_remove = set()
        direction = None
        for i, (x, y) in enumerate(ordered):
            dx, dy = lines[i]
            if not dx or not dy:
                direction = None
                value = atan2(dy, dx)
                continue
            new_direction = (dx>0), (dy>0)
            if new_direction != direction:
                direction = new_direction
                value = atan2(dy, dx)
            else:
                if value - atan2(dy, dx) > 0:
                    to_remove.add(i)
                value = atan2(dy, dx)
        
        return [tree for i, tree in enumerate(ordered) if i not in to_remove]
