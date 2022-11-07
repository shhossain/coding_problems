#include <bits/stdc++.h>
using namespace std;


int MaxSubarraySum(vector<int> nums, int k)
{
    unordered_set<int> map;
    int left = 0, res = -1, sum = 0;
    for(int right = 0; right<nums.size(); right++)
    {
        while(left < right && (map.count(nums[right]) || map.size() >= k))
        {
            sum -= nums[left];
            map.erase(nums[left]);
            left++;
        }
        sum +=nums[right];
        map.insert(nums[right]);
            
        if (map.size() == k)
            res = max(res, sum);
    }
    return res;
}


int main(){
    vector<int> a = {1,5,4,2,9,9,9};
    int k = 3;
    cout << MaxSubarraySum(a,k) << endl;

}