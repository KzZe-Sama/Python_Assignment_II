# Algorithm
def CSV(filename,data):
    accept=open(f"{filename}.csv","w")
    accept.write("name,address,age")
    accept.write("\n")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j !=len(data[i])-1:
                accept.write(f"{data[i][j]}")
                accept.write(",")
            else:
                accept.write(f"{data[i][j]}")
        if i!=len(data)-1:
            accept.write("\n")
    accept.close()

# data
dataA=[('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# Input
file=input("Enter A File Name:")
CSV(file,dataA)