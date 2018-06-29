word = input("Pick a word! ")

histogram_dict = {

}

for char in word:
    histogram_dict[char] = word.count(char)

print(histogram_dict)