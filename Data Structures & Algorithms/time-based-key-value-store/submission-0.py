class TimeMap:
    def __init__(self):
        self.store = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        timeline = self.store[key]
        ans = ""
        l = 0
        r = len(timeline) - 1
        while l <= r:
            m = (l + r) // 2
            if timeline[m][0] <= timestamp:
                ans = timeline[m][1] 
                l = m + 1            
            else:
                r = m - 1             
                
        return ans