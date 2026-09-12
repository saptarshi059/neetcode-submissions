class Solution:
    def _check_speed(self, k, piles, h):
        hrs = 0
        for idx in range(len(piles)):
            if piles[idx] <= k:
                hrs += 1
            elif piles[idx] % k == 0:
                hrs += (piles[idx] // k)
            else:
                hrs += (piles[idx] // k) + 1
        print(k, hrs)
        if hrs <= h:
            return True
        else:
            return False
    
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_speed, max_speed = 1, max(piles)
        while min_speed <= max_speed:
            k = (min_speed + max_speed) // 2
            # if k allows koko to consume all bananas, try to find an even smaller speed.
            if self._check_speed(k, piles, h):
                max_speed = k - 1
            else:
                min_speed = k + 1

        return min_speed
