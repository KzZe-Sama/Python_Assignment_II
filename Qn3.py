String=input("Enter A String: \n")
String=String.strip()
Words=String.split(" ")
anagram=[]
# Adding Anagrams To List As Tuple
for i in range(len(Words)):
    for j in range(len(Words)):
        if Words[i]!=Words[j]:
            a=sorted(Words[i].lower())
            b=sorted(Words[j].lower())
            if a==b:
                anagram.append((Words[i],Words[j]))

# Removing Duplicates
for x,y in anagram:
    for a,b in anagram:
        if x==b:
            anagram.remove((a,b))

print(anagram)