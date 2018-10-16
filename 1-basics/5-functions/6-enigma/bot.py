def run():
  print("Please enter a character to display...")
  cha=input()
  print("Please enter total number of characters...")
  num1=int(input())
  print("Please enter a whole number ...")
  num2=int(input())

  for i in range(0,num1,1):
     if (i+1%num2==0):
      print(cha,end="")
     else:
       print("-",end="") 
	


run()
