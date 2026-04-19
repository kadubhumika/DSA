class Solution(object):
    def maxDistance(self, nums1, nums2):

        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)

        max_dist = 0

        while i < n1 and j < n2:

            if nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1

        return max_dist