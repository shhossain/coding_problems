import heapq

class SortedList:
    def __init__(self):
        self._heap = []
    
    def append(self, item):
        heapq.heappush(self._heap, -item)
    
    def __getitem__(self, index):
        return self._heap[index]
    
    def __len__(self):
        return len(self._heap)

    def pop(self):
        return -heapq.heappop(self._heap)


for _ in range(int(input())):
    n = input()
    arr = map(int,input().split())
    srt = SortedList()
    total = 0
    for i in arr:
        if i != 0:
            srt.append(i)
        else:
            try:
                total += srt.pop()
            except IndexError:
                pass
    print(total)


