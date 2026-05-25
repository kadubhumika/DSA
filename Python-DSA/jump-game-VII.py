class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)

        queue = [0]
        farthest = 0

        while queue:

            curr = queue.pop(0)

            if curr == n - 1:
                return True

            front = max(curr + minJump, farthest)
            rear = min(curr + maxJump, n - 1)

            for i in range(front, rear + 1):

                if s[i] == '0':
                    queue.append(i)

            farthest = rear + 1

        return False