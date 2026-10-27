import random

def sort_list(nums):
    nums = nums.copy()
    n = len(nums)
    cnt = 0

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            cnt += 1
            if nums[j] < nums[min_index]:
                min_index = j

        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]

    return nums, cnt



lst_1 = [3, 47, 24, 0, -7]
lst_2 = [15, 2, 10, 8, 34, 5, 11, 33, 5, -6]

n = int(input())
lst_3 = []
for i in range(n):
  lst_3.append(random.randint(0, 100))

print(sort_list(lst_1))
print(sort_list(lst_2))
print(sort_list(lst_3))
