class Solution:
    def validSquare(self, p1, p2, p3, p4):

        def dist(a, b):

            return ((a[0] - b[0]) * (a[0] - b[0]) +
                    (a[1] - b[1]) * (a[1] - b[1]))

        dist_1 = dist(p1, p2)
        dist_2 = dist(p1, p3)
        dist_3 = dist(p1, p4)
        dist_4 = dist(p2, p3)
        dist_5 = dist(p2, p4)
        dist_6 = dist(p3, p4)

        arr = [dist_1, dist_2, dist_3,
               dist_4, dist_5, dist_6]

        arr.sort()

        # first 4 = sides
        # last 2 = diagonals

        if (arr[0] > 0 and
            arr[0] == arr[1] == arr[2] == arr[3] and
            arr[4] == arr[5]):

            return True

        return False