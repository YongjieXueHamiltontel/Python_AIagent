/* C (O(n²) time, O(1) extra space) */
/* Uses the LeetCode-style signature with malloc’d return array */
#include <stdlib.h>

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    for(int i = 0; i < numsSize - 1; ++i){
        for(int j = i + 1; j < numsSize; ++j){
            if (nums[i] + nums[j] == target) {
                int* res = malloc(2 * sizeof(int));
                res[0] = i;
                res[1] = j;
                *returnSize = 2;
                return res;
            }
        }
    }
    *returnSize = 0;
    return NULL;  // no solution
}

/*
Example:
int sz;
int* ans = twoSum(arr, n, target, &sz);
// use ans[0], ans[1] then free(ans);
*/
