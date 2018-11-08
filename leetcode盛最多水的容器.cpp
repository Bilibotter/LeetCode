#超越98%,下面有大神解
class Solution {
public:
	int maxArea(vector<int>& height) {
		int head=0, tail,left,right,square,ans=0;
		tail = height.size() - 1;
		while (tail > head)
		{
			left = height[head];
			right = height[tail];
			if (left>right)
			{
				square =(tail-head)*right;
				tail -= 1;
			}
			else
			{
				square = (tail - head)*left;
				head += 1;
			}
			ans = ans > square ? ans : square;
		}
		return ans;
	}
};
# 神解
class Solution {
public:
	int maxArea(vector<int>& heights) {
		int head=0, tail, square=0;
		tail = heights.size() - 1;
		while (tail > head)
		{
			square = max(square, (tail - head)*min(heights[head], heights[tail]));
			heights[head] > heights[tail] ? tail--:head++;
		}
        return square;
	}
};
