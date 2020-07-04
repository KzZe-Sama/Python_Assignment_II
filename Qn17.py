def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a//b
def square(a,b):
    return a**b

if __name__=="__main__":
    print("Welcome To My Calculator:")
    try:
        x = int(input("Enter First Number: "))
        y = int(input("Enter Another Number:"))
    except ValueError:
        print("Enter Only Integer Values.")
    else:
        print("What Operation You Want To Proceed?")
        print(
            f"1 =Add {x} and {y}\n- = Subtract {x} and {y}\n* = Multiply {x} and {y} \n/ = Divide {x} and {y}\n^ = {x} power {y}")
        ask = input()
        if ask == "+":
            print(add(x, y))
        elif ask == "-":
            print(subtract(x, y))
        elif ask == "*":
            print(multiply(x, y))
        elif ask == "/":
            try:
                print(divide(x, y))
            except ZeroDivisionError as e :
                print(e)

        elif ask == "^":
            print(square(x, y))
        else:
            print("Error No Such Operator")
    finally:
        print("Thank You For Using This Calculator, Have A Good Day Bye!")





