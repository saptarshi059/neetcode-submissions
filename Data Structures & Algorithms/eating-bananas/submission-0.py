class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_speed(k, h, piles):
            # This function checks whether all piles can be consumed inside h hours with speed k
            total_hrs = 0
            for p in piles:
                if p % k == 0:
                    total_hrs += (p // k)
                else:
                    total_hrs += (p // k) + 1
            if total_hrs <= h:
                return True
            else:
                return False

        # The value of k, doesn't need to be a value inside piles. It can be anything between at least, 1 and, at most, the largest pile number.
        
        L, R = 1, max(piles)
        # k = Rate of eating
        min_k = float("inf")
        while L <= R:
            k = (L+R) // 2
            if check_speed(k, h, piles):
                # This means, that the current k rate, is sufficient. I am now trying to find a smaller rate.
                min_k = min(min_k, k)
                R = k - 1
            else:
                # This means that the current k rate is insufficient. So, I need a faster rate
                L = k + 1

        return min_k