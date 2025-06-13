int maxArea(int* height, int heightSize) {
    int left = 0;
    int right = heightSize - 1;
    int maxarea = 0;

    while (left < right) {
        int width = right - left;

        
        int minheight;
if (height[left] < height[right]) {
    minheight = height[left];
} else {
    minheight = height[right];
}

        int area = minheight * width;

        if (area > maxarea) {
            maxarea = area;
        }

        
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxarea;
}
