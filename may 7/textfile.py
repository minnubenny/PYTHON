# Open the file and read the text
with open("/home/minnu/Desktop/week 1/may 7/hello.txt", "r") as file:
    text = file.read()

# Make all words lowercase
text = text.lower()

# Remove punctuation 
for char in ".,!?;:\n":
    text = text.replace(char, " ")

# Split the text into words
words = text.split()

# Count each word
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word counts
for word, count in word_count.items():
    print(word, ":", count)
