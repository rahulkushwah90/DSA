'''
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".
'''
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    if not s.islower():
        s = s.lower()
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome('RAHUL'))
