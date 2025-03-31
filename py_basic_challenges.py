'''
----------------------------------------------------------------------------
Challenge: 01-addOne
Difficulty: Basic

Prompt:
Write a function called addOne that takes a single number as an argument and 
returns that number plus 1.

Examples:

addOne(1) //=> 2
addOne(-5) //=> -4
-----------------------------------------------------------------------------
// Your solution for 01-addOne here:

'''
def add_one(num):
    return num + 1

'''
/*-----------------------------------------------------------------------------
Challenge: 02-addTwoNumbers

Difficulty: Basic

Prompt:

- Write a function called addTwoNumbers that accepts two numeric arguments and 
  returns the sum of those two numbers.
- If either argument is not a number, return the value of NaN.

Examples:

addTwoNumbers(5, 10) //=> 15
addTwoNumbers(10, -2) //=> 8
addTwoNumbers(0, 0) //=> 0
addTwoNumbers('Hello', 5) //=> NaN
-----------------------------------------------------------------------------*/
// Your solution for 02-addTwoNumbers here:
'''
def add_two_numbers(num1, num2):
    
    if isinstance(num1, int) and isinstance(num2,int):
        return num1 + num2
    else:
        return "please enter only numbers as parameters"

'''
/*-----------------------------------------------------------------------------
Challenge: 03-sumNumbers

Difficulty: Basic

Prompt:

- Write a function called sumNumbers that accepts a single array of numbers and 
  returns the sum of the numbers in the array.
- If the array is empty, return 0 (zero).

Examples:

sumNumbers([10]) //=> 10
sumNumbers([5, 10]) //=> 15
sumNumbers([2, 10, -5]) //=> 7
sumNumbers([]) //=> 0
-----------------------------------------------------------------------------*/
// Your solution for 03-sumNumbers here:    

'''
def sum_numbers(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    result = 0
    for el in nums:
        result += el
    return result

# print(sum_numbers([]))

'''
/*-----------------------------------------------------------------------------
Challenge: 04-addList

Difficulty: Basic

Prompt:

- Write a function called addList that accepts any quantity of numbers as 
  arguments, adds them together, and returns the resulting sum.
- Assume all parameters will be numbers.
- If called with no arguments, return 0 (zero).

Examples:

addList(1) //=> 1
addList(1,50,1.23) //=> 52.23
addList(7,-12) //=> -5
-----------------------------------------------------------------------------*/
// Your solution for 04-addList here:

'''
def add_list(*args):
    if len(args) == 0:
        return 0
    sum = 0
    for num in args:
        sum += num
    return sum 
# print(add_list(100,30,23,34,56,1.4))

'''
/*-----------------------------------------------------------------------------
Challenge: 05-computeRemainder

Difficulty: Basic

Prompt:

- Write a function named computeRemainder that accepts two numeric arguments 
  and returns the remainder of the division of those two numbers.
- The first argument should be the dividend, and the second argument should be 
  the divisor.
- If a 0 is passed in as the second argument, you should return JavaScript's 
  special numeric value: Infinity.
- For extra fun, complete this challenge without using the modulus (%) operator.

Examples:

computeRemainder(10,2) //=> 0
computeRemainder(4,0) //=> Infinity
computeRemainder(10.5, 3) //=> 1.5
-----------------------------------------------------------------------------*/
// Your solution for 05-computeRemainder here:
'''
import math
def compute_reminder(dividen, divisor):
    quotient = math.floor( dividen / divisor)
    reminder = dividen - (divisor * quotient) 
    return reminder

# print(compute_reminder(10,3))
'''
/*-----------------------------------------------------------------------------
Challenge: 06-range

Difficulty: Basic

Prompt:

- Write a function called ranging that accepts two integers as arguments and 
  returns an array of integers starting with the first argument up to one 
  less than the second argument.
- The range function must be called with the first argument less than or equal 
  to the second argument; otherwise, return the string "First argument must be 
  less than second".

Examples:

range(1,4) //=> [1,2,3]
range(-2, 3) //=> [-2,-1,0,1,2]
range(1,1) //=> []
range(5,2) //=> "First argument must be less than second"
-----------------------------------------------------------------------------*/
// Your solution for 06-range here:

'''
def ranging(num1, num2):
    num_range = []
    for i in range(num1, num2):
        num_range.append(i)
    if len(num_range) == 0:
        return "First argument must be less than second"
    return num_range

# print(ranging(-2,6))

'''

/*-----------------------------------------------------------------------------
Challenge: 07-reverseUpcaseString

Difficulty: Basic

Prompt:

- Write a function called reverseUpcaseString that accepts a single string 
  argument.
- The reverseUpcaseString function should return the string with its characters 
  in reverse order and convert all characters to uppercase.

Examples:

reverseUpcaseString("SEI Rocks!") //=> "!SKCOR IES" 
-----------------------------------------------------------------------------*/
// Your solution for 07-reverseUpcaseString here:

'''

def reverse_up_case_string(str):
    reverse_str = []
    for i in list(str):
        reverse_str.insert(0,i)
    return ','.join(reverse_str).upper()

# print(reverse_up_case_string('archile'))

'''
/*-----------------------------------------------------------------------------
Challenge: 08-removeEnds

Difficulty: Basic

Prompt:

- Write a function called removeEnds that accepts a single string argument, 
  then returns a string with the first and last characters removed.
- If the length of the string argument is less than 3, return an empty string.

Examples:

removeEnds('SEB Rocks!') //=> "EB Rocks"
removeEnds('a') //=> "" (empty string)
-----------------------------------------------------------------------------*/

'''
def remove_ends(string):
    if len(string) < 3:
        return ''
    list_string = list(string)
    sliced_str =  list_string[1:-1]
    return ''.join(sliced_str)

# print(remove_ends('SEB Rocks!'))

'''
/*-----------------------------------------------------------------------------
Challenge: 09-charCount

Difficulty: Basic

Prompt:

- Write a function named charCount that accepts a single string argument and 
  returns an object that represents the count of each character in the string.
- The returned object should have keys representing the character with its 
  value set to the number of times the character appears in the string argument.
- Upper and lower case characters should be counted separately.
- Space characters should be counted too.

Examples:

charCount('hello') 
//=> { h: 1, e: 1, l: 2, o: 1 }

charCount('Today is fantastic!') 
//=> { 
  T: 1, 
  o: 1, 
  d: 1, 
  a: 3, 
  y: 1, 
  ' ': 2, 
  i: 2, 
  s: 2, 
  f: 1, 
  n: 1, 
  t: 2, 
  c: 1, 
  '!': 1 
}
-----------------------------------------------------------------------------*/
// Your solution for 09-charCount here:

'''
# define return object
# create list from string
# loop over list:
    # If idx not in object add it as key
    # Else add +1 to properti

def char_count(str):
    count_obj ={}
    for i in list(str):
        if i in count_obj:
            count_obj[i] += 1
        else:
            count_obj[i] = 1
    return count_obj

# print(char_count("hello  Hello"))


'''
/*-----------------------------------------------------------------------------
Challenge: 10-formatWithPadding

Difficulty: Basic

Prompt:

- Write a function called formatWithPadding that accepts three arguments:
  - A numeric argument (an integer) representing the number to format.
  - A string argument (a single character) representing the character used to 
    "pad" the returned string to a minimum length.
  - Another numeric argument (an integer) representing the length to pad
    the returned string to.
- The function should return the integer as a string, left padded to the 
  length of the 3rd arg using the character provided in the 2nd arg.
- If the length of the integer converted to a string is equal or greater than 
  the 3rd argument, no padding is needed - just return the integer as a string.

Examples:

formatWithPadding(123, '0', 5) //=> "00123"
formatWithPadding(42, '*', 10) //=> "********42"
formatWithPadding(1234, '*', 3) //=> "1234"
-----------------------------------------------------------------------------*/
// Your solution for 10-formatWithPadding here:
'''
# 3 arguments,
# arg1: int to format , arg2: char use to pad, arg3: lenght to pad the return string to
# while return str is not arg3 value, insert padding character to the left
def format_with_padding(number,char_pad,length):
    try:
        float(number)
    except ValueError:
        return "enter a valid number in at first argument"
    try: 
        float(length)
    except ValueError:
        return "Enter a valud number at the last argument"
    
    if len(str(number)) >= length:
        return number
    formatted_array = list(str(number))
    while len(formatted_array) != length:
        formatted_array.insert(0,char_pad)
    
    return ''.join(formatted_array)

print(format_with_padding(123,'0',5))
