"""
Problem C. Bathroom Stalls
"""
import heapq


class MaxHeapObj(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)


def solve(N, K):
    N, K = int(N), int(K)
    heap = [MaxHeapObj(N)]
    table = {N: 1}
    while K > 0 and heap:
        empty = heapq.heappop(heap).val
        maxS, minS = empty // 2, empty // 2 - 1 + (empty & 1)
        if maxS:
            if maxS not in table:
                heapq.heappush(heap, MaxHeapObj(maxS))
            table[maxS] = table.get(maxS, 0) + table[empty]
        if minS:
            if minS not in table:
                heapq.heappush(heap, MaxHeapObj(minS))
            table[minS] = table.get(minS, 0) + table[empty]
        K -= table.pop(empty)
    return maxS, minS

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()

    T = int(f.readline())
    for case in range(1, T + 1):
        N, K = f.readline().strip().split()
        maxS, minS = solve(N, K)
        print("Case #{0}: {1} {2}".format(case, maxS, minS))
