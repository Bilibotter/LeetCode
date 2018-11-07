#include<vector>
#include<list>
#include<stack>
using namespace std;
class Solution {
public:
	int trap(vector<int>& height) {
		if (height.size() == 0)
		{
			return 0;
		}
		int rain=0,maxLeft = 0,maxRight=0,accumul=0,m,i=0,h,minHeight;
		vector<int> s;
		for (;i<height.size();i++)
		{
			if (maxLeft < height[i])
			{
				maxLeft = height[i];
			}
			s.push_back(maxLeft);
		}
		i = s.size() - 1;
		for (;i>=0;i--)
		{
			m = s[i];
			h = height[i];
			if (maxRight < h)
			{
				maxRight= h;
			}
			if (maxRight > m)
			{
				accumul = m - h;
			}
			else
			{
				accumul = maxRight - h;
			}
			if (accumul>0)
			{
				rain += accumul;
			}
		}
		return rain;
	}
};
