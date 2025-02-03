# a = 112
# print (type(a))
# b = 11.2
# print (type(b))
# v = "khaing"
# print (type(v))

# yourName = input ('What is your name?: ')
# print (yourName)

# yourNumber = input ("Enter a number: ")
# print ("Got it")
# yourNumber2 = input ("Enter another number: ")
# bool = input("Do you want addition or substraction?: ")
# if bool == "addition":
#  print (int(yourNumber)+float(yourNumber2))

# else :
#     print (int(yourNumber)-int(yourNumber2))

# var = 4000
# yourVar = input ("Give me a number: ")
# answerVar = var + int(yourVar)
# print ("Guess what the original value was!")
# if answerVar < 2000:
#     print ("It is much far away from the original value.")
# elif answerVar >4225:
#     print ("It's getting close to 5000.")
# else :
#     print ("Better try next time!")

# import array
# thislist = [0.9, 9.9, 8.9, 34]
# print (thislist[0]+thislist[1])

# print (type(thislist))
# thislist.pop(3)
# print(thislist)
# thislist.insert (0, 0.7)
# print(thislist)
# print(thislist.index(9.9))

# thislist.extend(3)
# print(thislist)


# import array
# arr = [(4,45, 433, 456] 

# arr.sort()
# print(arr)
# ans = sum(int(arr[0])+int(arr[7]))
# print(ans)

# print("Wake up " * 7)

# for element in range (7):
#     print("wake up baby!")

# for element in range (2,4,6):
#     print(element)

# arr = ["Breakfast", "Snack", "Lunch" , "Dinner", "Supper"]

# for element in arr:
#     element = "Delicious "+ element

#     print (element)

# for i in range (0, len (arr)): # starting index number is declared first then the length of which array you are carrying out this operation
#     if arr[i] == "Snack": #arr[i] should be used to indicate that index number of that element
#         continue
#     arr[i] = "I will eat "+ arr[i]
#     print (arr[i])

# code is not working here!

# for i in range (0, len(arr)):
    

#     arr [i] == "I will not eat " + arr[i]
   
# print (arr[i])

#Finding the tallest person in the room.

# #Ask for age input
# x = input ("How tall are you?: " )
# # for answer in range (8):
# #      print (answer*30.48)
# if x < 5:
#     print (x*30.48)
# elif x > 8:
#     print (x)
import math


lst = []

x      = int(input("Can you enter how many apples you have bought?: "))
a      = int(input("Can you enter how many oragnges you have bought?: "))
c      = int(input("Can you enter how many mangoes you have bought?: "))

xprice = int (input("Can you tell me how much an apple is?: "))
aprice = int (input("Can you tell me how much an orange is?: "))
cprice = int (input("Can you tell me how much a mango is?: "))

apple = x * xprice
orange = a*aprice
mango = c*cprice
lst =[apple,orange,mango]


# xprice = int (input("Can you tell me how much did apples cost?: "))
# aprice = int (input("Can you tell me how much did oranges cost?: "))
# cprice = int (input("Can you tell me how much did mangoes cost?: "))



# lst = [xprice, aprice, cprice] 

answer = int (sum(lst))
print (answer)
print("Yout total cost is {} units.".format(answer))




