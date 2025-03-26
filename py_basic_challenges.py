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

print(sum_numbers([]))