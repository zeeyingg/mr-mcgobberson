'''
Given an array of ints, return True if 6 appears as either the first or last
element in the array. The array will be length 1 or more.
'''

def first_last6(nums):
  return (nums[0] == 6 or nums[len(nums)-1] == 6)

print("=====FIRST LAST 6=====")
print(first_last6([1, 2, 3]))
print("...should be False")
print(first_last6([13, 6, 1, 2, 3]))
print("...should be False")


'''
Given an array of ints, return True if the array is length 1 or more, and
the first element and the last element are equal.
'''

def same_first_last(nums):
  return (len(nums) >= 1 and nums[0] == nums[len(nums)-1])

print("=====SAME FIRST LAST=====")
print(same_first_last([1,2,3]))
print("...should be False")
print(same_first_last([1,2,3, 1]))
print("...should be True")
print(same_first_last([1,2,1]))
print("...should be True")


'''
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
'''

def make_pi():
  pi = [3,1,4]
  return (pi)

print("=====MAKE PI=====")
print(make_pi())
print("...should be [3, 1, 4]")


'''
Given 2 arrays of ints, a and b, return True if they have the same first
element or they have the same last element. Both arrays will be length 1
or more.
'''

def common_end(a, b):
  return (a[0] == b[0] or a[len(a)-1] == b[len(b)-1])

print("=====COMMON END=====")
print(common_end([1, 2, 3], [7,3]))
print("...should be True")
print(common_end([1, 2, 3], [7,3, 2]))
print("...should be False")
print(common_end([1, 2, 3], [1,3]))
print("...should be True")


'''
Given an array of ints length 3, return the sum of all the elements.
'''

def sum3(nums):
  return nums[0] + nums[1] + nums[2]

print("=====SUM3=====")
print(sum3([1, 2, 3]))
print("...should be 6")
print(sum3([5, 11, 2]))
print("...should be 18")
print(sum3([7, 0, 0]))
print("...should be 7")


'''
Given an array of ints length 3, return an array with the elements "rotated
left" so {1, 2, 3} yields {2, 3, 1}.
'''

def rotate_left3(nums):
  new = [nums[1],nums[2],nums[0]]
  return new

print("=====ROTATE LEFT 3=====")
print(rotate_left3([1, 2, 3]))
print("...should be [2,3,1]")
print(rotate_left3([5, 11, 9]))
print("...should be [11,9,5]")
print(rotate_left3([7, 0, 0]))


'''
Given an array of ints length 3, return a new array with the elements in reverse
order, so {1, 2, 3} becomes {3, 2, 1}.
'''

def reverse3(nums):
  new = [nums[2],nums[1],nums[0]]
  return new

print("=====REVERSE 3=====")
print(reverse3([1, 2, 3]))
print("...should be [3,2,1]")
print(reverse3([5, 11, 9]))
print("...should be [9,11,5]")
print(reverse3([7, 0, 0]))
print("...should be [0,0,7]")


'''
Given an array of ints length 3, figure out which is larger, the first or last
element in the array, and set all the other elements to be that value. Return
the changed array.
'''

def max_end3(nums):
  maxthing = max(nums[0],nums[2])
  new = [maxthing,maxthing,maxthing]
  return new

print("=====MAXEND3=====")
print(max_end3([1,2,3]))
print("...should be [3,3,3]")
print(max_end3([11,5,9]))
print("...should be [11,11,11]")
print(max_end3([2,11,3]))
print("...should be [3,3,3]")


'''
Given an array of ints, return the sum of the first 2 elements in the array.
If the array length is less than 2, just sum up the elements that exist,
returning 0 if the array is length 0.
'''

def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  return nums[0] + nums[1]

print("=====SUM2=====")
print(sum2([1,2,3]))
print("...should be 3")
print(sum2([1,1]))
print("...should be 2")
print(sum2([1,1,1, 1]))
print("...should be 2")


'''
Given 2 int arrays, a and b, each length 3, return a new array length 2
containing their middle elements.
'''

def middle_way(a, b):
  middle = [a[1],b[1]]
  return middle

print("=====MIDDLE_WAY=====")
print(middle_way([1, 2, 3], [4, 5, 6]))
print("...should be [2,5]")
print(middle_way([7, 7, 7], [3, 8, 0]))
print("...should be [7,8]")
print(middle_way([5, 2, 9], [1, 4, 5]))
print("...should be [2,4]")


'''
Given an array of ints, return a new array length 2 containing the first and
last elements from the original array. The original array will be length 1 or
more.
'''

def make_ends(nums):
  frist = [nums[0],nums[len(nums)-1]]
  return frist

print("=====MAKE ENDS=====")
print(make_ends([1, 2, 3]))
print("...should be [1,3]")
print(make_ends([1, 2, 3, 4]))
print("...should be [1,4]")
print(make_ends([7, 4, 6, 2]))
print("...should be [7,2]")


'''
Given an int array length 2, return True if it contains a 2 or a 3.
'''
def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False

print("=====HAS 23=====")
print(has23([2, 5]))
print("...should be True")
print(has23([4, 3]))
print("...should be True")
print(has23([4, 5]))
print("...should be False")
