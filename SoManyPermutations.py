# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
# Create as many "shufflings" as you can!
# Examples:
# With input 'a':
# Your function should return: ['a']
# With input 'ab':
# Your function should return ['ab', 'ba']
# With input 'abc':
# Your function should return ['abc','acb','bac','bca','cab','cba']
# With input 'aabb':
# Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
# Note: The order of the permutations doesn't matter.

def permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perms = set()

        for i, c in enumerate(s):
            rest = s[:i] + s[i+1:]
            for perm in permutations(rest):
                perms.add(c + perm) 

    return list(perms) 
