def word_count(sentence):
    words = sentence.split()
    word_freq = {word: words.count(word) for word in words}
    return len(words), word_freq

sentence = "i am indranil i am"
count, frequency = word_count(sentence)
print(f"The number of words in the sentence is: {count}")
print("Word frequency:", frequency)

