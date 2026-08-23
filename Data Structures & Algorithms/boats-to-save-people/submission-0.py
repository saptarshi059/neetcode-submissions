class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people) - 1
        L, R = 0, n
        boats = 0
        while L <= R:
            s = people[L] + people[R]
            if s <= limit:
                boats += 1
                L += 1
                R -= 1
            else:
                boats += 1
                R -= 1
        
        return boats
