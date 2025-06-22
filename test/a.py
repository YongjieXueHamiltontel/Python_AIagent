# Python (O(n) time, O(n) space)
def two_sum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        comp = target - num
        if comp in lookup:
            return [lookup[comp], i]
        lookup[num] = i
    return []  # no solution

# Example
# >>> two_sum([2, 7, 11, 15], 9)
# [0, 1]
