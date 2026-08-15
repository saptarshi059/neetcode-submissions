class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # time-to-reach
        def ttr(pair, target):
            return (target - pair[0]) / pair[1]
        
        array = list(zip(position, speed))
        array = sorted(array, key = lambda x: x[0])

        fleets = 1
        ahead_ttr = ttr(array[-1], target) # Means, the car ahead
        for i in range(len(array) - 2, -1, -1):
            before_ttr = ttr(array[i], target) # Means, the car before

            # This means that the car ahead is going slower than the car behind
            if ahead_ttr < before_ttr:
                fleets += 1
                ahead_ttr = before_ttr

        return fleets