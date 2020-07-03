# Datas
DataA=['Ram','Shaym','Sita','Raghav']
DataB=['John','Kenndy','Thomas']

print("Data A: ",DataA)
print("Data B: ",DataB)
flag=False
# For Data A
print("Checking in John in DataA:")
for value in DataA:
    if value.upper()=="JOHN":
        print("John Exists in DataA")
        flag=True
        break

if flag==False:
    print("John Doesnot Exist in Data A")

    print("Checking in John in DataB:")
    for value in DataB:
        if value.upper() == "JOHN":
            print("John Exists in DataB")
            flag = True
            break

if flag==False:
    print("John Doesnot Exist in DataB")
