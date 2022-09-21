'''
Given a string and a non-negative int n, 
return a larger string that is n copies of the original string.
'''

def string_times(str, n):
  return (str*n)

print("=====STRING TIMES=====")
print(string_times('Hi', 2))
print("...should be HiHi")
print(string_times('Hi', 3))
print("...should be HiHiHi")

'''
Given a string and a non-negative int n, 
we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. 
Return n copies of the front;
'''

def front_times(str, n):
  if (len(str) > 2):
    return (str[0:3] * n)
  return (str*n)

print("=====FRONT TIMES=====")
print(front_times('Chocolate', 2))
print("...should be ChoCho")
print(front_times('Chocolate', 3))
print("...should be ChoChoCho")

'''
Given a string, return a new string made of every other char 
starting with the first, so "Hello" yields "Hlo".
'''

def string_bits(str):
  new = ""
  for index in range(len(str)):
    if (index % 2 == 0):
      new += str[index]
  return (new)

print("=====STRING BITS=====")
print(string_bits('Hello'))
print("...should be Hlo")
print(string_bits('Hi'))
print("...should be H")

'''
Given a non-empty string like "Code" return a string like "CCoCodCode"
'''

def string_splosion(str):
  new = ""
  for index in range(len(str)+1):
    new += str[0:index]
  return (new)

print("=====STRING SPLOSION=====")
print(string_splosion('Code'))
print("...should be CCoCodCode")
print(string_splosion('abc'))
print("...should be aababc")

'''
Given a string, return the count of the number of times 
that a substring length 2 appears in the string and also as the last 2 chars of the string, 
so "hixxxhi" yields 1 (we won't count the end substring).
'''

def last2(str):
  last = str[len(str)-2:len(str)]
  count = 0
  for index in range(len(str)-2):
    if (str[index:index+2] == last):
      count+=1
  return count

print("=====LAST2=====")
print(last2('hixxhi'))
print("...should be 1")
print(last2('xaxxaxaxx'))
print("...should be 1")

'''
Given an array of ints, return the number of 9's in the array.
'''

def array_count9(nums):
  count = 0
  for i in nums:
    if (i == 9):
      count+=1
  return count

print("=====ARRAY COUNT9=====")
print(array_count9([1, 2, 9]))
print("...should be 1")
print(array_count9([1, 9, 9]))
print("...should be 2")

'''
Given an array of ints, return True 
if one of the first 4 elements in the array is a 9. 
The array length may be less than 4.
'''

def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4

  for i in range(end):
    if nums[i] == 9:
      return True
  return False

print("=====ARRAY FRONT9=====")
print(array_front9([1, 2, 9, 3, 4]))
print("...should be True")
print(array_front9([1, 2, 3, 4, 9]))
print("...should be False")

'''
Given an array of ints, return True 
if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''

def array123(nums):
  end = len(nums)-2

  for i in range(end):
    if (nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3):
      return True
  return False

print("=====ARRAY123=====")
print(array123([1, 1, 2, 3, 1]))
print("...should be True")
print(array123([1, 1, 2, 4, 1]))
print("...should be False")

'''

Given 2 strings, a and b, return the number of the positions 
where they contain the same length 2 substring. 
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" 
substrings appear in the same place in both strings.
'''

def string_match(a, b):
  count = 0
  end = len(a)-1

  for i in range(end):
    if (a[i:i+2] == b[i:i+2]): # a1:b1 denotes a splicing of strings (exclusive of the last value)
      count+=1

  return count

print("=====STRING MATCH=====")
print(string_match('xxcaazz', 'xxbaaz'))
print("...should be 3")
print(string_match('abc', 'abc'))
print("...should be 2")
