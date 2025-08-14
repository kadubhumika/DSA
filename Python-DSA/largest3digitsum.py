class Solution(object):
    def largestGoodInteger(self, num):
        largest = ""
        for i in range(len(num) - 2):

            if num[i] == num[i + 1] == num[i + 2]:
                triplet = num[i:i + 3]
                if triplet > largest:
                    largest = triplet
        return largest
