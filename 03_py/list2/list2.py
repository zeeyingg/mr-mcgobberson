def count_evens(nums):
  count = 0
  for i in nums:
    if i%2 == 0:
      count+= 1
  return count

print("Should return 3:")
print(count_evens([2, 1, 2, 3, 4]))
print("Should return 3:")
print(count_evens([2, 2, 0]))
print("Should return 0:")
print(count_evens([1, 3, 5]))

def big_diff(nums):
    numsmin = nums[0]
    numsmax = nums[0]
    for i in nums:
        if i < numsmin:
            numsmin = i
        if i > numsmax:
            numsmax = i
    return numsmax - numsmin

print("Should return 7:")
print(big_diff([10, 3, 5, 6]))
print("Should return 8:")
print(big_diff([7, 2, 10, 9]))
print("Should return 8:")
print(big_diff([2, 10, 7, 2]))

def centered_average(nums):
    numsmin = nums[0]
    numsmax = nums[0]
    indexmin= 0
    indexmax = 0
    index = 0
    for i in nums:
        if i < numsmin:
            numsmin = i
            indexmin = index
        if i >= numsmax:
            numsmax = i
            indexmax = index
        index+=1
    count = 0
    for i in range(len(nums)):
        if i != indexmin and i != indexmax:
            count += nums[i]
    return int(count / (len(nums)-2))

print("Should return 3:")
print(centered_average([1, 2, 3, 4, 100]))
print("Should return 5:")
print(centered_average([1, 1, 5, 5, 10, 8, 7]) )
print("Should return -3:")
print(centered_average([-10, -4, -2, -4, -2, 0]))

def sum13(nums):
  sum = 0
  for i in range(len(nums)):
    if i == 0 and nums[i] != 13:
      sum += nums[i]
    elif nums[i] != 13 and nums[i-1] != 13:
      sum += nums[i]
  return sum

print("Should return 6:")
print(sum13([1, 2, 2, 1]))
print("Should return 2:")
print(sum13([1, 1]))
print("Should return 6:")
print(sum13([1, 2, 2, 1, 13]))

def sum67(nums):
  sum = 0
  sixy = False
  for i in nums:
    if i == 6:
      sixy = True
    if sixy == False:
      sum += i
    if i == 7:
      sixy = False
  return sum

print("Should return 6:")
print(sum67([1, 2, 2]))
print("Should return 2:")
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print("Should return 6:")
print(sum67([1, 1, 6, 7, 2]))

def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False

print("Should return True:")
print(has22([1, 2, 2]))
print("Should return False:")
print(has22([1, 2, 1, 2]))
print("Should return 6:")
print(has22([2, 1, 2]))
