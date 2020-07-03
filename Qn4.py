# List
Data=[]
print("ID before adding",id(Data))
# Append
Data.append("Freak")
Data.append("Anubis")
Data.append("Shiro")
Data.append("Atul")
Data.append("ZekKen")
Data.append("Praz")

print(Data)
print("ID:",id(Data))
print("First Data: ",Data[0])
print("First Data ID: ",id(Data[0]))
print("Second Data: ",Data[1])
print("Second Data ID: ",id(Data[1]))
# Sort
Data=sorted(Data)
print("Sorted Data:")
print(Data)
print("First Data: ",Data[0])
print("First Data ID: ",id(Data[0]))
print("Second Data: ",Data[1])
print("Second Data ID: ",id(Data[1]))