# Algorithm
def CSV():
    data=[]
    accept=open("clear.csv","r")
    line1=accept.readline()
    line1=line1.strip()
    ListCol=line1.split(",")
    lines = accept.readlines()
    a, b = str(lines[0]), str(lines[1])
    a, b = a.strip(), b.strip()
    c = [tuple(a.split(',')), tuple(b.split(','))]
    for i, j, k in c:
        e = {}
        e[ListCol[0]], e[ListCol[1]], e[ListCol[2]] = i, j, int(k)
        data.append(e)
    print(data)
    accept.close()
if __name__=="__main__":
    CSV()