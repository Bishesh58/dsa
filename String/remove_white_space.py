''''
Question: remove white space from a given string.
'''
def remove_space(s):
    arr = []
    for i, item in enumerate(s):
        if not (item == ' ' or item == '\t' or item == '\n'):
            arr.append(item)

    return ''.join(arr)


def remove_space(s):
    result = []

    for char in s:
        if char not in (' ', '\t', '\n'):
            result.append(char)

    return ''.join(result)


input_string = "Hello Test"
print(remove_space(input_string))

# Time:O(n) space: O(n)

#using: split & join
def remove_space(s):
    return ''.join(s.split()) 
    
# Time:O(n) space: O(n) creates list of words for extra space

# using build in method
def remove_space(s):
    new_s = ""
    for item in s:
        if(not item.isspace()):
            new_s+=item
    return new_s


string = 'Hello bishesh    test '
print(remove_space(string))

# Time:O(n) space: O(n) 