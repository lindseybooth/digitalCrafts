#1

# for number in range(1,11):
#     print(number)

#2

# print("Pick a number!")
# n = input()
# print("Pick another number!")
# m = input()

# for number in range(int(n), int(m)):
#     print(number)

#3
# for number in range(1, 11):
#     if number % 2 != 0:
#          print(number)

#4
# myList = " ***** "
# print(myList * 5)

#5
# print('Enter a number between 1 - 10')
# userInput = input()
# userInputInt = int(userInput)
# myList = []

# x = 0
# while x < userInputInt:
#     myList.append('*')
#     x += 1

# for character in myList:
#     print(character * userInputInt)

#6

# width = int(input("Enter a number between 1 and 10 "))
# height = int(input('Enter a number between 1 and 10 '))

# print('*' * width)

# num_spaces = width - 2
# spaces = ' ' * num_spaces
# for number in range(height - 2):
#     print('*' + spaces + "*")

# print('*' * width)

#7
# def pypart(n):
     
#     for number in range(0, n):
#         for number2 in range(0, number+2):
#             print("* ",end="")
#         print("\r")
# n = 7
# print(pypart(n))

#8
# height = int(input('Enter a number between 1 and 10 '))

# def pypart(n):
     
#     for number in range(0, n):
#         for number2 in range(0, number+2):
#             print("* ",end="")
#         print("\r")
# n = height
# print(pypart(n))

#9
for outerIndex in range(1,11):
    for innerIndex in range(1, 11):
        sum = int(outerIndex) * int(innerIndex)
       
        print("{} * {} = ".format(outerIndex, innerIndex) + str(sum))
