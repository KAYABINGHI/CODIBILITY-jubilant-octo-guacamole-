# Given a list containing n distinct numbers from 0 to n; find the missing number; Input: [3, 0, 1]; Output: 2

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) / 2  # Sum of numbers from 0 to n
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Test
print(missing_number([3, 0, 1]))  # Output: 2

