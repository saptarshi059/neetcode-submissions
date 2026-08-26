class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check_capacity(c, weights, days):
            shipped = []
            idx = 0
            for d in range(days):
                total_day = 0
                while idx < len(weights):
                    total_day += weights[idx]
                    if total_day <= c:
                        shipped.append(weights[idx])
                        idx += 1
                    else:
                        break
                
                if len(shipped) == len(weights):
                    return True

            return False

        L, R = 1, sum(weights)
        min_cap = float("inf")
        while L <= R:
            cap = (L + R) // 2
            if check_capacity(cap, weights, days):
                min_cap = min(cap, min_cap)
                R = cap - 1
            else:
                L = cap + 1
        
        return min_cap
