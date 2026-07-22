from collections import deque
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        queue = deque(range(len(tickets)))
        time = 0

        while tickets[k] > 0:

            front = queue.popleft()

            tickets[front] -= 1
            time += 1

            if tickets[front] > 0:
                queue.append(front)

        return time
