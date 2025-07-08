class FindSumPairs(private val nums1: IntArray, private val nums2: IntArray) {

    fun add(index: Int, `val`: Int) {
        nums2[index] += `val` // Add value to nums2 at the given index
    }

    fun count(tot: Int): Int {
        var Count = 0
        for (i in nums1.indices) {
            val target = tot - nums1[i]
            for (j in nums2.indices) {
                if (nums2[j] == target) {
                    Count++
                }
            }
        }
        return Count
    }
}
