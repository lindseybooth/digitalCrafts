#1
# def hello (name):
#     print("Hello " + name)

# hello("Igor")

 #2
# import matplotlib.pyplot as plot 

# def f(x): 
#     return x + 1 

# xs = list(range(-3, 3)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#3
# import matplotlib.pyplot as plot 
# def f(x):
#     return x * x

# xs = list(range(-100, 100))
# ys = []

# for x in xs:
#     ys.append(f(x))

# plot.plot(xs,ys)
# plot.show()

#4
# import matplotlib.pyplot as plot 

# def f(x): 
#     if x % 2 == 0:
#         return -1 

#     if x % 2 != 0:
#         return 1

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.bar(xs, ys) 
# plot.show()

#5
# import matplotlib.pyplot as plot 
# import math 

# def f(x): 
#     return math.sin(x) 

# xs = list(range(-5, 5)) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()



#6
# import matplotlib.pyplot as plot 
# from numpy import arange
# import math

# def f(x): 
#     return math.sin(x) 

# xs = arange(-5, 6, 0.1) 
# ys = [] 

# for x in xs: 
#      ys.append(f(x)) 

# plot.plot(xs, ys) 
# plot.show()

#7
# import matplotlib.pyplot as plot 

# def tempConversion(x): 
#     return x * 1.8 +32 

# xs = list(range(0, 100)) 
# ys = [] 

# for x in xs: 
#      ys.append(tempConversion(x)) 

# plot.plot(xs, ys) 
# plot.show()

#8
# choice = input("Do you want to play again? Y or N? ")

# def playAgain():
#     if choice == "Y":
#         print(True)
#     else:
#         print(False)
# playAgain()  

# #9
choice = input("Do you want to play again? Y or N? ")

def playAgain():
    if choice == "Y":
        print(True)
    elif choice == "N":
        print(False)
    else:
        print("Invalid Input!")
playAgain() 




# #Class Practice

# # def myFirstFunction(myName):
# #     print ("Hello " + myName)

# # # myFirstFunction() #calls function

# # for repetition in range(0, 10):
# #     myFirstFunction("Lindsey")
# #Printed function 10 times

# # result= 0
# # pi = 3.14
# # def circumfrence(radius):
# #     result = 2 * pi * radius
# #     print(result)

# # circumfrence(2)
# # circumfrence(12.234)

# # result= 0
# # pi = 3.14
# # def circumfrence(radius):
# #     result = 2 * pi * radius
# #     return(result)

# # a = circumfrence(2)
# # print(a * 4)
# # b = circumfrence(23)
# # print (b * 2)


# # result= 0
# # pi = 3.14
# # def circumfrence(radius, diameter, number):
# #     result = 2 * pi * radius * diameter
# #     return(result)

# # a = circumfrence(2)
# # print(a * 4)
# # b = circumfrence(23)
# # print (b * 2)

# printed_hello = "False"

# def display_hello():
#   print('Hello')
#   printed_hello = "True"

# print("before function gets called: " + printed_hello)

# display_hello()

# print("after function gets called: " + printed_hello)