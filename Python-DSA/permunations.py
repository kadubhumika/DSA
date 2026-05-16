class Solution:
    def permute(self, nums):
        ans = []

        def backtrack(path):

            # base case
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for num in nums:

                # skip already used numbers
                if num in path:
                    continue

                # choose
                path.append(num)

                # recurse
                backtrack(path)

                # backtrack
                path.pop()

        backtrack([])
        return ans