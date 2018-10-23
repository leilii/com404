

print("Please enter a word:")
myword=input()
print("Please enter one of folowing options 1-2:")
print("1) Display in a Box") # display the word in an ascii art box"
print("2) Display Lower-case") # display the word in lower-case e.g. hello 
print("3) Display Upper-case") # display the word in upper-case e.g. HELLO 
print("4) Display Mirrored") #display the word with its mirrored word e.g. Hello | olleH 
print("5) Repeat ")#ask the user how many times to display the word and then display the 
myChoice=int(input())
while  myChoice>5 or myChoice<1:
  print("Please enter a number from 2 to 5...")
  myChoice=int(input())

#function for action1
def function1(myword):
  w_len=len(myword)+2
  star=""
  for i in range (1,w_len,1):
    star+="*"
  print(star)
  print("\n")
  print(myword)

#function for action2
def function2(myword):
   print(myword.lower())

#function for action3
def function3(myword):
   print(myword.upper())

#function for action4
def function4(myword):
  newword=""
  for i in range(len(myword),1,-1):
      newword+=myword[i]
  print(newword)
  return(newword)
   
#function for action5
def function5(myword):
   print("How manytimes would you like to repeat the word:")
   rep=int(input())
   for i in range(1,rep,2):
     print(myword.lower())
     print(myword.upper())


if myChoice==1:
  function1(myword)
elif myChoice==2:
 function2(myword)   
elif myChoice==3:
 function3(myword) 
elif myChoice==4:
 function4(myword) 
elif myChoice==5:
 function5(myword)  


 
