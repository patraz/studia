nums = [1,2,3,1]

def is_twice(nums):
    return len(set(nums)) != len(nums)

print(is_twice(nums))