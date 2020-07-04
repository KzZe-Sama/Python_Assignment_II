def valid_parenthese(str1):
    stock, characters = [], {"(": ")", "{": "}", "[": "]"}
    for parenthese in str1:
        if parenthese in characters:
            stock.append(parenthese)
        elif len(stock) == 0 or characters[stock.pop()] != parenthese:
            return False
    return True




# Input
user_input = input("Enter: ")

print(valid_parenthese(user_input))
