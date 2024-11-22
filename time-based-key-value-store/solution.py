def binary_search(array, target):
    left, right = 0, len(array)-1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

class TimeMap:

    def __init__(self):
        self.value_map = {}
        self.timestamp_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.value_map:
            self.value_map[key] = []
            self.timestamp_map[key] = []
        
        self.value_map[key].extend([value])
        self.timestamp_map[key].extend([timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp_map:
            return ""
            
        pos = binary_search(self.timestamp_map[key], timestamp)
        if pos == -1:
            return ""
        return self.value_map[key][pos]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
