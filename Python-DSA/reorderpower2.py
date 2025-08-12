class Solution(object):
    def reorderedPowerOf2(self, n):

        s = sorted(str(n))

        for i in range(30):
            power_of_2 = 1 << i
            if sorted(str(power_of_2)) == s:
                return True

        return False
