# Solution
#  Runtime: 98%
#  Memory usage: 54%
#
# Description
#
#  You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.
#
#    For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
#
# You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.
#
# Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.
#

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        
        to_stops = defaultdict(list)
        
        for i, route in enumerate(routes):
            for stop in route:
                to_stops[stop].append(i)
        
        queue = deque([(i, 1) for i in to_stops[source]])
        seen_routes = {i for i in to_stops[source]}
        seen_stops = {source}

        while queue:
            route, total = queue.popleft()
            
            if route in to_stops[target]:
                return total
              
            for stop in routes[route]:
                if stop not in seen_stops:
                    seen_stops.add(stop)
                    
                    for other_route in to_stops[stop]:
                        if other_route not in seen_routes:
                            seen_routes.add(other_route)
                            queue.append((other_route, total + 1))
        return -1
