// C++ (O(n) time, O(n) space)
#include <vector>
#include <unordered_map>
using namespace std;

vector<int> twoSum(const vector<int>& nums, int target) {
    unordered_map<int, int> lookup;
    for (int i = 0; i < (int)nums.size(); ++i) {
        int comp = target - nums[i];
        auto it = lookup.find(comp);
        if (it != lookup.end())
            return {it->second, i};
        lookup[nums[i]] = i;
    }
    return {};  // no solution
}

/*
Example:
vector<int> res = twoSum({2,7,11,15}, 9);
// res == {0,1}
*/
