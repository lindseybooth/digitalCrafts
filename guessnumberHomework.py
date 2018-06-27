# # 1
# number = 5

# while True:
#      print("I am thinking of a number between 1 and 10. What's the number?")
#      guess = input()
#      num = int(guess)

#      if num == number:    
#          print('You won!')
#          break
#      else:
#          print("Nope, try again! What's the number?")


# # 2
# while True:
#     print("I am thinking of a number between 1 and 10. What's the number?")
#     guess = input()
#     num = int(guess)

#     if num == number:    
#         print('You won!')
#         break
#     elif num > 5:
#         print("Your guess is too high. Try again!")
#     elif num < 5:
#         print("Your guess is too low. Try again!")

#3

# import random
# number = random.randint(1, 10)

# while True:
#     print("I am thinking of a number between 1 and 10. What's the number?")
#     guess = input()
#     num = int(guess)

#     if num == number:    
#         print('You won!')
#         break
#     elif num > number:
#         print("Your guess is too high. Try again!")
#     elif num < number:
#         print("Your guess is too low. Try again!")


#4

# import random
# number = random.randint(1, 10)

# count = 1
# while True:
#     print("I am thinking of a number between 1 and 10. What's the number?")
#     guess = input()
#     num = int(guess)
    
#     if num == number:    
#         print('You won!')
#         break
#     elif num > number:
#         print("Your guess is too high. Try again!")
#     elif num < number:
#         print("Your guess is too low. Try again!")

#     count += 1
#     if count == 6:
#         print("You only had five guesses. You lose!")
#         break
        