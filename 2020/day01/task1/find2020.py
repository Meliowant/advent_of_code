#!/usr/bin/python3

nums = []
with open("input.txt") as f:
    num = f.readline()
    while num != '':
        nums.append(int(num))
        num = f.readline()

nums.sort()
print (f"Read {len(nums)} values")

last_less_then_half_pos = 0
for n in nums:
    if n < 1010:
        last_less_then_half_pos += 1
    else:
        break
print(f"Last smaller value in pos: {last_less_then_half_pos}")
print(nums[:last_less_then_half_pos + 1])

for bigger in nums[last_less_then_half_pos + 1: ]:
    exp_smaller = 2020 - bigger
    # print(f"Checking if {exp_smaller} exists")
    if exp_smaller in nums[:last_less_then_half_pos + 1]:
        print(bigger * exp_smaller)

for num1 in nums:
    for num2 in nums[nums.index(num1)+1: ]:
        third = 2020-num1-num2
        if third in nums[(nums.index(num2)+1) : ]:
            print(num1*num2*(2020-num1-num2))
