import heapq

def solve(n, k, A, B, C, D):
    min_heap = [A]
    a_i = A
    
    for i in range(1, n):
        a_i = (B * a_i + C) % D
        if len(min_heap) < k:
            heapq.heappush(min_heap, a_i)
        elif a_i > min_heap[0]:
            heapq.heapreplace(min_heap, a_i)

    return [heapq.heappop(min_heap) for _ in range(k)]

n, k, A, B, C, D = map(int, input().strip().split())
print(*solve(n, k, A, B, C, D))