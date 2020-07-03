# Algorithm
# Camel Cased
def snake_cased(String):
    result=String[0].lower()
    for i in range(1,len(String)):
        if String[i].isupper():
            result=result+"_"+String[i].lower()
        else:
            result=result+String[i]
    return result
# Algorithm Kebab Cases
def kebab_cases(String):
    result=String[0].lower()
    for i in range(1,len(String)):
        if String[i].isupper():
            result=result+"-"+String[i].lower()
        else:
            result=result+String[i]
    return result
# Input
data=input("Enter A String:")
print("Snaked Cased:",snake_cased(data))
print("Kebab Cases:",kebab_cases(data))
