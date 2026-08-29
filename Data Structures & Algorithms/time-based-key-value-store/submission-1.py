class TimeMap:

    def __init__(self):
        self.ds = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.ds:
            self.ds[key] = []
        
        self.ds[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds:
            return ""

        key_list = self.ds[key]

        # 1. Run binary search on the timestamps
        l, r = 0, len(key_list) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if key_list[mid][1] <= timestamp:
                res = key_list[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res