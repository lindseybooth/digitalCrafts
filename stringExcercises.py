# #1
# str = "hello world!"
# print(str.upper())

# #2
# str2 = "hello world!"
# print(str2.title())

# #3
# str3 = "hello world!"
# print(str3[::-1])

#4

# str4 = "Given a paragraph of text as a string, print the paragraph in leetspeak. To translate a string to leetspeak, you need to replace make the following character replacements"
# if str4.find('a') >= 0:
#     str4 = str4.replace('a', '4')
# if str4.find('e') >= 0:
#     str4 = str4.replace('e', '3')
# if str4.find('d') >= 0:
#     str4 = str4.replace('g', '6')
# if str4.find('i') >= 0:
#     str4 = str4.replace('i', '1')
# if str4.find('o') >= 0:
#     str4 = str4.replace('o', '0')
# if str4.find('s') >= 0:
#     str4 = str4.replace('s', '5')
# if str4.find('e') >= 0:
#     str4 = str4.replace('t', '7')

# print(str4)

#5

# print("Pick a word!")
# word = input()
# if word.find('a') >=0:
#     word = word.replace('a', 'aaaaa')
# if word.find('e') >=0:
#     word = word.replace('e', 'eeeee')
# if word.find('i') >=0:
#     word = word.replace('i', 'iiiii')
# if word.find('o') >=0:
#     word = word.replace('o', 'ooooo')
# if word.find('u') >=0:
#     word = word.replace('u', 'uuuuu')

# print(word)

#6 skipping for now
# print("Enter a sentence to decipher!")
# sentence = input()
# print(sentence)


# while 1:
#     print("Enter a sentence to decipher!")
#     phrase = input()
#     if phrase == "" : break
#     print("Here it is your phrase, encrypted:")
#     print(phrase.encode("rot_13"))
# print("Have a nice afternoon!")

cipher = "lbh zhfg hayrnea jung lbh unir yrnearq"

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

position = 0
newPosition = 0

finalString = " "

for cipherLetter in cipher:
    if cipherLetter.isspace() == False:
        position = alphabet.index(cipherLetter)
        newPosition = position - 13
        if newPosition < 0:
            newPosition = 26 + newPosition
        finalString = finalString + alphabet[newPosition]
       
print(finalString)






