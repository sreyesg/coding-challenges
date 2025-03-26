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

print(compute_reminder(10,3))

