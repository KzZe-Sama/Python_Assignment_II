def alog_anagram(String):
    String=String.strip()
    for i in range(len(String)):
        if String[i]==" ":
            String.replace(String[i],"")

    print(String)

text=input("Enter Text:\n")
alog_anagram(text)