class Solution:

    def get_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums: list[int]) -> int:

        nums_list = []
        current_max = nums[0]

        for num in nums:
            if num > current_max:
                current_max = num

            current_gcd = self.get_gcd(num, current_max)
            nums_list.append(current_gcd)

        nums_list.sort()

        left = 0
        right = len(nums_list) - 1
        total_gcd_sum = 0

        while left < right:
            pair_gcd = self.get_gcd(nums_list[left], nums_list[right])
            total_gcd_sum += pair_gcd

            left += 1
            right -= 1

        return total_gcd_sum
