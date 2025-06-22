// JavaScript (O(n) time, O(n) space)
function twoSum(nums, target) {
    const lookup = new Map();
    for (let i = 0; i < nums.length; i++) {
        const comp = target - nums[i];
        if (lookup.has(comp)) {
            return [lookup.get(comp), i];
        }
        lookup.set(nums[i], i);
    }
    return [];  // no solution
}

// Example:
// console.log(twoSum([2,7,11,15], 9)); // [0, 1]
