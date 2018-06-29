sentence = input("Write a sentence: ")

histogram_dict = { }

sentence_histogram = sentence.split()

for word in sentence_histogram:
    histogram_dict[word] = sentence.count(word)

print(histogram_dict)