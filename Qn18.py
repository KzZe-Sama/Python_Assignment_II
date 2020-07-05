import json

# Inspecting JSON library
# print(dir((json)))

# print(help(json))

data={"name":"Aayush","age":19}
print("Data: ",data)
# Serializing A Dictionary to a Json File
json_string = json.dumps(data,indent=2)
print("After Serializing")
print(json_string)

#  Deserialize the json file
print("After De-Serializing")
result=json.loads(json_string)
print(result)


