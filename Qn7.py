# Tuple
dataA=("Aayush","KC",19)
dataB=("Vidur","Khanal",18)
dataC=("Saroj","Koirala",20)
dataD=("Keyur","Dhungana",None)
dataE=("Manish","Shrestha",22)

ListOfData=[]
# Appending all Tuple to list
ListOfData.append(dataA)
ListOfData.append(dataB)
ListOfData.append(dataC)
ListOfData.append(dataD)
ListOfData.append(dataE)

total=0
count=0
for i in range(len(ListOfData)):
    age=ListOfData[i][2]
    if age != None:
        total=total+age
    else:
        count=count+1
avg=total/(len(ListOfData)-count)
print("Average Age =",avg)

for value in ListOfData:
    age=value[-1]
    if age !=None:
        age=float(age)
        if age<avg:
            print(value[0],value[1],"Younger")
        else:
            print(value[0], value[1], "Older")
