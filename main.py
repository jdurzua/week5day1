#######################paired programmming###############################
print("Herminio, Josue, and Emmanuel present...")
# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[5])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.find('c'))
# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[0:13:2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote 
quote="Ask not what your country can do for you — ask what you can do for your country.- John F. Kennedy"
result = quote.find("John F. Kennedy")
print(quote[82:])
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
(info.find("subjective"))
print(info[36:])
# b. Extract every third word.
print(info[0::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
print(info[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: 
may="MAY THE FORCE BE WITH YOU."
print(may.lower())
# String Joining and Splitting:

word_list = ("Make", "haste", "slowly.")
new_list = " ".join(word_list)
print(new_list)
# b. Now, split the string at every occurrence of the letter 'a'.

# Replacing Words:
sen = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(sen.replace("busy","distracted"))
# b. Replace "plans" with "mistakes".
print(sen.replace('plans','mistakes'))
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
L = 'Iteration '
print(L * 7)