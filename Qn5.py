# Tuple
dataA=("Aayush","KC",19)
dataB=("Vidur","Khanal",19)
dataC=("Saroj","Koirala",20)
dataD=("Manish","Shrestha",22)

ListOfData=[]
# Appending all Tuple to list
ListOfData.append(dataA)
ListOfData.append(dataB)
ListOfData.append(dataC)
ListOfData.append(dataD)
print(ListOfData)
def sort_key_fname(data):
    return data[0]
def sort_key_lname(data):
    return data[1]
def sort_key_age(data):
    return data[2]

print("Sorting Using First Name: ")
ListOfData.sort(key=lambda a:a[0])
print(ListOfData)
print("Sorting Using Last Name: ")
ListOfData.sort(key=lambda a:a[1])
print(ListOfData)
print("Sorting Using Age: ")
ListOfData.sort(key=lambda a:a[2])
print(ListOfData)