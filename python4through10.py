# #4

# print("Pick a number between 0 and 6, inclusive!")
# number = input()
# day = int(number)

# if day == 0:
#     print("Sunday")
# elif day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")

# #5
# print("Pick a number between 0 and 6, inclusive!")
# number = int(input())


# if number > 0 and number < 6:
#     print("Go to work!")
# else:
#     print("Sleep in!")

#6
# print("Enter a number in degrees Celsius and it will be converted to degrees Farenheit")
# number = input()
# degrees = int(number)

# Farenheit = (degrees * 1.8) + 32

# print(Farenheit)

#7
# print("What is the total bill amount")
# number = input()
# bill = float(number)

# print("How was the service? You can choose 'good', 'fair', or 'bad.'")
# service = input()

# if service == 'good':
#     sum = bill * .2
#     total = sum + bill
#     print(total)
#     print("Your tip amount is " + str(sum))
#     print("Your total bill is " + str(total))

# elif service == 'fair':
#     sum = bill * .15
#     total = sum + bill
#     print(total)
#     print("Your tip amount is " + str(sum))
#     print("Your total bill is " + str(total))

# elif service == 'bad':
#     sum = bill * .1
#     total = sum + bill
#     print(total)
#     print("Your tip amount is " + str(sum))
#     print("Your total bill is " + str(total))

#8
# print("What is the total bill amount")
# number = input()
# bill = float(number)

# print("How was the service? You can choose 'good', 'fair', or 'bad.'")
# service = input()

# print("How many people are splitting this bill?")
# split = input()

# if service == 'good':
#     sum = bill * .2
#     total = (sum + bill) / int(split)
#     print("Your total tip amount is " + str(sum))
#     print("Each person owes " + str(total))

# elif service == 'fair':
#     sum = bill * .15
#     total = (sum + bill) / int(split)
#     print("Your total tip amount is " + str(sum))
#     print("Each person owes " + str(total))

# elif service == 'bad':
#     sum = bill * .1
#     total = (sum + bill) / int(split)
#     print(total)
#     print("Your total tip amount is " + str(sum))
#     print("Each person owes " + str(total))


#9
# for number in range(0,11):
#     print(number)

#10
# count = 0
# while True:
#     print("You currently have no coins. Do you want a coin? Y/N")
#     question = input()
#     if question == "Y":
#         count += 1
#         print("You currentlly have " + str(count) + " coins")
#     elif question == "N":
#         count += 0
#         print("You currentlly have " + str(count) + " coins")
#         break