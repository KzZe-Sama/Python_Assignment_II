class RealNum:
    def check(self,data):
        result=[]
        # First Iteration for first element
        for x in data:
            # Iteration for 2nd element
            for y in data:
                # Iteration for third elemen
                for z in data:
                    sum=x+y+z
                    # If some of three numbers is equal to 0
                    if sum==0:
                        result.append([x,y,z])
                        # Removing if x y z are used once
                        data.remove(x)
                        data.remove(y)
                        data.remove(z)
        return result

x = [-25, -10, -7, -3, 2, 4, 8, 10]
obj=RealNum()
print(obj.check(x))

