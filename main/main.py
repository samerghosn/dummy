# encoding=utf8
#####################################
#### PART 9: FUNCTION EXERCISES #####
#####################################


# Complete the tasks below by writing functions! Keep in mind, these can be
# really tough, its all about breaking the problem down into smaller, logical
# steps. If you get stuck, don't feel bad about having to peek to the solutions!

#####################
## -- PROBLEM 1 -- ##
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# For example:
# arrayCheck([1, 1, 2, 3, 1])  True
# arrayCheck([1, 1, 2, 4, 1]) False
# arrayCheck([1, 1, 2, 1, 2, 3])  True
#another file goes here
def arrayCheck(nums):
    correct_count = 0
    i = 0
    while i < len(nums):
        print("i" + str(i)  )

        if (i > 0 and (nums[i] == 2 or correct_count > 0) and correct_count !=2) :
            x=nums[i-1]+1
            if nums[i] == x:
                correct_count = correct_count+1
            else:
                correct_count = 0
        elif correct_count == 2:
            break
        i=i+1
    if correct_count == 2:
        print ("found it")
    else:
        print ("not there")

#arrayCheck([1, 1, 2, 1, 2, 3])
#####################
## -- PROBLEM 2 -- ##
#####################

# Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".

# For example:

# stringBits('Hello') → 'Hlo'
# stringBits('Hi') → 'H'
# stringBits('Heeololeo') → 'Hello'

def stringBits(str):
  # CODE GOES HERE
  mylist=list(str)
  mystr=''
  for elm in range(0, len(str),2):
      mystr=mystr+mylist[elm]
  print(mystr)


#stringBits('Heeololeo')
#####################
## -- PROBLEM 3 -- ##
#####################

# Given two strings, return True if either of the strings appears at the very end
# of the other string, ignoring upper/lower case differences (in other words, the
# computation should not be "case sensitive").
#
# Note: s.lower() returns the lowercase version of a string.
#
# Examples:
#
# end_other('Hiabc', 'abc') → True
# end_other('AbC', 'HiaBc') → True
# end_other('abc', 'abXabc') → True


def end_other(a, b):
  # CODE GOES HERE
  last_three=(a[-3:])
  if last_three.lower() == b.lower():
        print(True)
  else: print(False)

  
#end_other('abcdef', 'DEf')
#####################
## -- PROBLEM 4 -- ##
#####################

# Given a string, return a string where for every char in the original,
# there are two chars.

# doubleChar('The') → 'TThhee'
# doubleChar('AAbb') → 'AAAAbbbb'
# doubleChar('Hi-There') → 'HHii--TThheerree'

def doubleChar(str):
  # CODE GOES HERE
  i=0
  newlist=""
  while (i<len(str)):
      newlist += str[i]+str[i]
      i=i+1
  print(newlist)

doubleChar('Hi-There')
#####################
## -- PROBLEM 5 -- ##
#####################

# Read this problem statement carefully!

# Given 3 int values, a b c, return their sum. However, if any of the values is a
# teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
# and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
# takes in an int value and returns that value fixed for the teen rule.
#
# In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
# Define the helper below and at the same indent level as the main no_teen_sum().
# Again, you will have two functions for this problem!
#
# Examples:
#
# no_teen_sum(1, 2, 3) → 6
# no_teen_sum(2, 13, 1) → 3
# no_teen_sum(2, 1, 14) → 3

def no_teen_sum(a, b, c):
  # CODE GOES HERE
  print (1)

def fix_teen(n):
  # CODE GOES HERE
  print (1)
#####################
## -- PROBLEM 6 -- ##
#####################

# Return the number of even integers in the given array.
#
# Examples:
#
# count_evens([2, 1, 2, 3, 4]) → 3
# count_evens([2, 2, 0]) → 3
# count_evens([1, 3, 5]) → 0

def count_evens(nums):
  # CODE GOES HERE
  print (1)
