'''
/*-----------------------------------------------------------------------------
Challenge: 11-isPalindrome

Difficulty: Intermediate

Prompt:

- Write a function called isPalindrome that accepts a single string argument, 
  then returns true or false depending upon whether or not the string is a 
  palindrome.
- A palindrome is a word or phrase that is the same forward or backward.
- Casing and spaces are not included when considering whether or not a string 
  is a palindrome.
- If the length of the string is 0 or 1, return true.

Examples:

isPalindrome('SEI Rocks') //=> false
isPalindrome('rotor') //=> true
isPalindrome('A nut for a jar of tuna') //=> true
isPalindrome('') //=> true
-----------------------------------------------------------------------------*/
// Your solution for 11-isPalindrome here:

'''
# validate string length to 0 or 1
# force lower case
# eliminate spaces
# find reverse string method
# compare return bool

def is_palindrome(str):
    if len(str) <= 1:
        return True
    reference_str = str.replace(" ","").lower()
    difference_str = []
    for  idx in list(reference_str):
        difference_str.insert(0,idx)
    
    if reference_str == ''.join(difference_str):
        return True
    else:
        return False
    
# print(is_palindrome('A nut for a jar of tuna'))

'''
/*-----------------------------------------------------------------------------
Challenge: 12-hammingDistance

Difficulty: Intermediate

Prompt:

In information theory, the hamming distance refers to the count of the 
differences between two strings of equal length. It is used in computer science 
for such things as implementing a "fuzzy search" capability.

- Write a function named hammingDistance that accepts two arguments, which are 
  both strings of equal length.
- The function should return the count of the symbols (characters, numbers, 
  etc.) at the same position within each string that are different.
- If the strings are not of the same length, the function should return NaN.

Examples:

hammingDistance('abc', 'abc') //=> 0
hammingDistance('a1c', 'a2c') //=> 1
hammingDistance('!!!!', '****') //=> 4
hammingDistance('abc', 'ab') //=> NaN
-----------------------------------------------------------------------------*/
// Your solution for 12-hammingDistance here:

'''
# evaluate that both strings are the same length
# define reference and difference lists
#loop over difference to compare against reference list
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        return "strings to compare don't have the same distance"
    reference = list(str1)
    difference = list(str2)
    index = 0
    distance = 0 

    def rHumming():
        nonlocal index, distance, reference
        
        if index == len(reference):
            return distance
        if difference[index] != reference[index]:
            distance += 1
        index += 1 
        
        return rHumming()
    return rHumming()

print(hamming_distance('12334','1a3as'))
        

