def calculateVolumeOfCuboid(length,width,height):
    cuboid=length*width*height
    return(cuboid)



def calculateVolOfCuboid(length2):
   
    return(calculateVolumeOfCuboid(length2,length2,length2))

def run():
   print("Please enter the length of cub")
   length3=int(input())
   return(calculateVolOfCuboid(length3))
   


print(run())

    
