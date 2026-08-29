class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = ([],[])
        
        self.ds[key][0].append(value)
        self.ds[key][1].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds:
            return ""

        states, ts = self.ds[key]

        # 1. Run binary search on the timestamps
        l,r = 0, len(ts) - 1
        while l <= r:
            mid = (l + r) // 2
            if int(ts[mid]) == timestamp:
                break
            elif int(ts[mid]) > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        
        if ts[mid] == timestamp:
            # Found target - return value associated with that timestamp
            return states[mid]
        
        # This means that we did not find the target - hence, we can return value associated with previous index
        if ts[r] < timestamp:
            return states[r]
        if (r - 1) < 0:
            return ""
            