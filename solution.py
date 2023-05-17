def binary_search(nums, target):
    index_low = 0
    index_high = len(nums) - 1
    while index_low <= index_high:
        index_mid = (index_low + index_high) // 2
        if nums[index_mid] == target:
            return index_mid
        elif nums[index_mid] < target:
            index_low = index_mid + 1
        else: 
            index_high = index_mid - 1
    return -1