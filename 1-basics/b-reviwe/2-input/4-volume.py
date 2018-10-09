import math
#ask user to enter a shape
print("Please enter a shap cy for cylander or co for cone")
#read user respond
shape=input()
#ask user for radius
print("Please enter a Radius")
Radius=float(input())
#ask user for hight
print("Please enter a hight")
Hight=float(input())

V1 = (math.pi *(pow(radius, 2))* Hight
#decide if the sape is cylander
if(shape=="cy"):
  print("The volum of the cylander with" + str(Radius)+"and hight"+Hight +"is"+round(V1,2))
elif(shap=="co"): 
  V2=V1/3
  print("The volum of the cone with" + str(Radius)+ "and hight"+Hight +"is" + round(V2,2))
