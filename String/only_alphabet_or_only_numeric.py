''''
Question: Check if a string contains only alphabetic characters.
'''

# Time O(n)
def only_alphabet(string):
    for char in string:
        if not char.isalpha():
            return False
    return True


result = only_alphabet("Bishesh")
print(result)

#  using ascii number
def only_alphabet(string):
    for char in string:
        if not ((65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)):
            return False
    return True


result = only_alphabet("Bishesh34")
print(result)

''''
Question: check if string contains only digits.
'''

def only_numeric(string):
    for char in string:
        if not char.isnumeric():
            return False
    return True


result = only_numeric("12")
print(result)

#  using ascii number
def only_numeric(string):
    for char in string:
        if not (48 <= ord(char) <= 57):
            return False
    return True


result = only_numeric("34")
print(result)