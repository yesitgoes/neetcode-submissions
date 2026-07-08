from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total_sum = 0
    for n in nums:
        total_sum += n
    return total_sum

def get_min(nums: List[int]) -> int:
    min_num = float("inf")
    for n in nums:
        if n < min_num:
            min_num = n
    return min_num

def get_max(nums: List[int]) -> int:
    max_num = float("-inf")
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
