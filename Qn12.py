# Algorithm
def is_palindrome(word):
    reverse=""
    word=word.upper()
    for value in word:
        reverse=value+reverse
    if reverse==word:
        return True
    else:
        return False

# Input
ask=input("Enter A Word:")

print("Palindrome=",is_palindrome(ask))