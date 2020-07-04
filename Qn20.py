class RealNum:
    def check(self,data):
        result=[]
        for x in data:
            for y in data:
                for z in data:
                    sum=x+y+z
                    if sum==0:
                        result.append([x,y,z])
                        data.remove(x)
                        data.remove(y)
                        data.remove(z)
        return result

x = [-25, -10, -7, -3, 2, 4, 8, 10]
obj=RealNum()
print(obj.check(x))

